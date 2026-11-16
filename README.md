# llm-hallucination

# Deteksi dan Mitigasi Halusinasi LLM pada Pertanyaan Layanan Publik Berbahasa Indonesia

Project mata kuliah [NAMA MATA KULIAH] | Kelompok [NO. KELOMPOK] | Dosen pengampu: [NAMA DOSEN]

Topik: Deteksi dan Mitigasi Halusinasi LLM

## Deskripsi

Project ini mengukur tingkat halusinasi Qwen3-1.7B (Instruct) pada pertanyaan layanan publik administrasi kependudukan dan dokumen berbahasa Indonesia, membangun detektor halusinasi berbasis konsistensi jawaban, dan mengevaluasi Retrieval-Augmented Generation (RAG) sebagai mitigasi.

## Ruang Lingkup

- Model yang diuji: Qwen3-1.7B Instruct (mode thinking dimatikan)
- Domain: layanan publik (paspor, KTP-el, KK, KIA, akta)
- Dataset pembanding: TruthfulQA (300 pertanyaan acak, seed 42)
- Label jawaban: Benar, Halusinasi, Tidak menjawab

## Skenario Eksperimen

| Kode | Deskripsi |
|---|---|
| S1 | Qwen3-1.7B tanpa RAG (baseline) |
| S2 | Qwen3-1.7B dengan RAG (mitigasi) |
| S3 | Detektor halusinasi berbasis konsistensi jawaban |
| S4 | Detektor S3 diuji pada TruthfulQA |

## Struktur Repositori

| Folder | Isi |
|---|---|
| data/raw/ | Dokumen sumber asli: imigrasi, dukcapil, truthfulqa |
| data/processed/ | Chunk dan dataset QA hasil olahan |
| notebooks/ | Notebook eksperimen (Google Colab) |
| src/ | Kode program yang dipakai ulang |
| docs/ | Tabel literatur, rencana evaluasi, laporan progress |

## Sumber Data

Daftar URL dan tanggal akses setiap dokumen dicatat di `data/README.md`. Kebenaran jawaban dinilai terhadap salinan dokumen pada tanggal akses tersebut.

## Cara Menjalankan

Akan dilengkapi pada Progress 3 setelah model baseline dijalankan.

## Status Progress

| Progress | Kegiatan | Status |
|---|---|---|
| 1 | Inisiasi dan rencana | Sedang dikerjakan |
| 2 | EDA dan persiapan data | Belum dimulai |
| 3 | Model baseline | Belum dimulai |
| 4 | Model utama | Belum dimulai |
| 5 | Eksperimen inti | Belum dimulai |
| 6 | Evaluasi dan analisis | Belum dimulai |
| 7 | Prototipe dan draf akhir | Belum dimulai |

## Anggota Kelompok

| No | Nama | NIM | Peran |
|---|---|---|---|
| 1 | Tonggi Simanjuntak | 42324006 | Ketua koordinasi & Integrasi |
| 2 | Joice | 42324002 | Data Pengumpulan & Prepocessing |
| 3 | Joy | 42324022 | Dokumentasi |
| 4 | Brahmana | 42324029 | Evaluasi |
| 5 | Rido | 42324030 | Modeling |
| 6 | Hesekiel | 42324050 | Data EDA & Visualisasi |

## Penggunaan AI Generatif

Claude (Anthropic) digunakan untuk diskusi perumusan project, penyusunan draf kerangka laporan, dan pembuatan draf pasangan tanya-jawab. Seluruh hasil diperiksa oleh anggota kelompok.