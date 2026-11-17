"""EDA awal 11 halaman layanan paspor imigrasi.go.id (Progress 2).
Pemakaian:  python eda_imigrasi.py data/raw/imigrasi docs
Keluaran :  docs/statistik_imigrasi.csv, docs/ringkasan_eda.json
Kata dihitung dengan pemisahan spasi (str.split)."""
import sys, glob, os, re, json, csv
from collections import Counter

src = sys.argv[1] if len(sys.argv) > 1 else "data/raw/imigrasi"
out = sys.argv[2] if len(sys.argv) > 2 else "docs"
os.makedirs(out, exist_ok=True)

META = {  # nama file (huruf kecil) -> (halaman, jenis layanan)
 "imigrasimasyarakatumum.txt": ("Masyarakat Umum", "Permohonan baru"),
 "imigrasianakdibawah17.txt": ("Anak di bawah 17 tahun", "Permohonan baru"),
 "imigrasianakdwikewarganegaraan.txt": ("Anak dwikewarganegaraan", "Permohonan baru"),
 "imigrasicalonpekerjamigran.txt": ("Calon pekerja migran", "Permohonan baru"),
 "imigrasihajiumroh.txt": ("Haji/umrah", "Permohonan baru"),
 "imigrasianaklahirdiluarnegri.txt": ("Anak lahir di luar negeri", "Permohonan baru"),
 "imigrasipasporakanhabismasaberlaku.txt": ("Paspor akan habis masa berlaku", "Penggantian"),
 "imigrasipasporhilang.txt": ("Paspor hilang", "Penggantian"),
 "imigrasipasporrusak.txt": ("Paspor rusak", "Penggantian"),

 "imigrasipenggantianpasporDiluarNegri.txt".lower(): ("Penggantian di luar negeri", "Penggantian"),
 "imigrasipengubahandatapaspor.txt": ("Pengubahan data paspor", "Penggantian"),
}
SECTIONS = ["Informasi Umum", "Prosedur", "Mekanisme Penerbitan", "Persyaratan", "Biaya"]

rows, core_lines = [], {}
for f in sorted(glob.glob(os.path.join(src, "*.txt")), key=lambda p: os.path.basename(p).lower()):
    name = os.path.basename(f)
    t = open(f, encoding="utf-8").read().replace("\r\n", "\n")
    s, e = t.find("Empty heading"), t.find("Terakhir Update")
    core = t[s:e] if 0 <= s < e else t
    upd = re.search(r"Terakhir Update\s*:\s*([^\n]+)", t)
    halaman, jenis = META.get(name.lower(), (name, "?"))
    rows.append({
        "file": name, "halaman": halaman, "jenis_layanan": jenis,
        "kata_total": len(t.split()), "karakter_total": len(t),
        "kata_inti": len(core.split()),
        "bagian_ditemukan": sum(bool(re.search(r"^\s*%s\s*$" % x, t, re.M)) for x in SECTIONS),
        "terakhir_update": upd.group(1).strip() if upd else "",
        "ada_url_di_file": t.lstrip().startswith("http"),
        "ada_tanggal_akses": bool(re.search(r"^\d\d/\d\d/\d{4}\s*$", t, re.M)),
        "jumlah_nominal_rp": len(re.findall(r"Rp\s?\d", t)),
    })
    core_lines[name] = {l.strip() for l in core.split("\n") if len(l.strip()) >= 40}

cnt = Counter(l for s in core_lines.values() for l in s)
tot_lines = sum(len(s) for s in core_lines.values())
dup_lines = sum(1 for s in core_lines.values() for l in s if cnt[l] >= 2)

with open(os.path.join(out, "statistik_imigrasi.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

kt = sum(r["kata_total"] for r in rows); ki = sum(r["kata_inti"] for r in rows)
summ = {
 "jumlah_file": len(rows), "kata_total": kt, "karakter_total": sum(r["karakter_total"] for r in rows),
 "kata_inti": ki, "persen_inti": round(100*ki/kt, 1),
 "rata_kata_total": round(kt/len(rows), 1), "min_kata_total": min(r["kata_total"] for r in rows),
 "maks_kata_total": max(r["kata_total"] for r in rows),
 "jenis": dict(Counter(r["jenis_layanan"] for r in rows)),
 "update": dict(Counter(r["terakhir_update"] for r in rows)),
 "tanpa_url": [r["file"] for r in rows if not r["ada_url_di_file"]],
 "dengan_tanggal_akses": [r["file"] for r in rows if r["ada_tanggal_akses"]],
 "baris_inti_unik_ge40": tot_lines, "baris_duplikat_antar_file": dup_lines,
 "persen_baris_duplikat": round(100*dup_lines/tot_lines, 1),
}
json.dump(summ, open(os.path.join(out, "ringkasan_eda.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(json.dumps(summ, indent=1, ensure_ascii=False))
for r in rows: print(r["halaman"], r["kata_total"], r["kata_inti"], r["bagian_ditemukan"], r["terakhir_update"], r["ada_url_di_file"], r["jumlah_nominal_rp"])
