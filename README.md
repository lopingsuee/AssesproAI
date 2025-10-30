# 🧠 AI Interview Assessment

Proyek ini merupakan sistem **AI Interview Assessment** berbasis **Speech-to-Text (Whisper)** dan **Natural Language Understanding (Sentence-BERT)**.  
Aplikasi dibangun menggunakan **Streamlit** sebagai UI untuk HR, dengan pipeline otomatis dari **video/audio → transkrip → skor performa & confidence**.

---

## 📁 Struktur Folder

```bash
ai-interview-assessment/
├─ app/
│  ├─ app.py                      # Entry Streamlit (UI)
│  ├─ components/                 # Komponen UI terpisah
│  │  ├─ __init__.py
│  │  ├─ inputs.py                # select QID, input link/upload
│  │  ├─ results.py               # panel JSON HR, download button, tables
│  │  └─ progress.py              # spinners, progress bars
│  ├─ pages/                      # (opsional) halaman tambahan streamlit
│  │  ├─ 1_Evaluation.ipynb       # halaman edukasi (notebook) – optional
│  │  └─ 2_Docs.md                # dokumentasi singkat
│  └─ __init__.py
│
├─ core/                          # Business logic (tanpa UI)
│  ├─ __init__.py
│  ├─ config.py                   # baca config.yaml & env vars
│  ├─ question_bank.py            # load YAML/JSON pertanyaan & ideal answers
│  ├─ downloader.py               # fetch video dari URL (yt-dlp, gdown, direct)
│  ├─ media.py                    # ekstraksi audio, normalisasi (ffmpeg/moviepy)
│  ├─ stt.py                      # Speech-to-Text (Whisper / faster-whisper)
│  ├─ nlp_preprocess.py           # cleaning, stopword, slang dict, stemming
│  ├─ language_router.py          # deteksi bahasa (fastText/langdetect/whisper)
│  ├─ similarity.py               # Sentence-BERT similarity
│  ├─ keywords.py                 # keyword coverage (must/nice)
│  ├─ structure.py                # skor struktur jawaban (intro-body-closing)
│  ├─ confidence.py               # gabungan ASR_conf, Lang_conf, Agree_conf, Len_conf
│  ├─ evaluator.py                # hitung PerformanceScore + ConfidenceScore
│  ├─ serializer.py               # compose output JSON untuk HR
│  └─ utils.py                    # helper umum (timer, io, text normalize)
│
├─ models/                        # cache/model artefacts
│  ├─ README.md
│  └─ (auto cached)               # SBERT, fastText lid.176.bin, dll.
│
├─ data/
│  ├─ question_bank.yaml          # definisi QID, ideal answer, keywords, weight
│  ├─ slang_dict.json             # kamus normalisasi (opsional)
│  ├─ stopwords_id.txt            # (opsional, jika custom)
│  └─ samples/                    # contoh video & GT untuk demo/test
│
├─ experiments/                   # notebook eksplorasi (bebas)
│  ├─ 01_whisper_eval.ipynb
│  ├─ 02_similarity_calibration.ipynb
│  └─ 03_streamlit_prototype.ipynb
│
├─ evaluation/                    # skrip evaluasi akurasi STT
│  ├─ compute_wer.py              # batch WER/CER → CSV + ringkasan
│  └─ datasets/
│     ├─ audio/                   # *.wav
│     └─ gt/                      # *.txt (ground truth)
│
├─ tmp/                           # artefak runtime (gitignore)
│  ├─ videos/                     # unduhan video mentah
│  ├─ audio/                      # wav 16k mono
│  └─ transcripts/                # txt/srt/json segmen
│
├─ logs/
│  └─ app.log                     # logging pipeline
│
├─ tests/
│  ├─ test_downloader.py
│  ├─ test_stt.py
│  ├─ test_evaluator.py
│  └─ test_confidence.py
│
├─ config.yaml                    # konfigurasi global (paths, model size, thresholds)
├─ requirements.txt               # dependensi
├─ .env.example                   # ENV (MODEL_SIZE, CUDA, API KEYS jika perlu)
├─ .gitignore
└─ README.md
```

---

## ⚙️ File Penting

### `requirements.txt`
```bash
streamlit
moviepy
ffmpeg-python
yt-dlp
requests
whisper
faster-whisper
sentence-transformers
langdetect
pyyaml
pandas
numpy
jiwer
Sastrawi
```

### `config.yaml`
Konfigurasi utama untuk model, path, dan bobot penilaian:
```yaml
app:
  title: "AI Interview Assessment"
  max_upload_mb: 200
paths:
  tmp_videos: "tmp/videos"
  tmp_audio: "tmp/audio"
  tmp_transcripts: "tmp/transcripts"
models:
  whisper_backend: "whisper"          # whisper | faster-whisper
  whisper_size: "base"                # tiny/base/small/medium
  sbert_name: "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
  langdetect: "fasttext"              # fasttext | langdetect | whisper
scoring:
  pass_threshold: 0.70
  weights:
    similarity: 0.55
    keyword_must: 0.30
    keyword_nice: 0.10
    structure: 0.05
confidence:
  asr_weight: 0.7
  lang_weight: 0.3
  min_len_tokens: 120
```

---

## 🚀 Cara Menjalankan

```bash
# 1. Buat virtual environment
python -m venv .venv
source .venv/bin/activate     # (Windows: .venv\Scripts\activate)

# 2. Install dependencies
pip install -r requirements.txt

# 3. Jalankan aplikasi Streamlit
streamlit run app/app.py
```

---

## 🧩 Deskripsi Singkat Modul Utama

| Folder | Fungsi |
|--------|---------|
| `app/` | Antarmuka Streamlit (UI HR) |
| `core/` | Logika utama: STT, NLP, scoring |
| `data/` | Bank pertanyaan & kamus teks |
| `evaluation/` | Pengujian akurasi STT (WER/CER) |
| `experiments/` | Eksperimen & notebook riset |
| `tmp/` | Artefak runtime (video/audio/temp) |
| `tests/` | Unit test modular |
| `models/` | Cache model SBERT / FastText |

---

> ✨ **Catatan tambahan:**
> - Target akurasi *Speech-to-Text (STT)* minimal **≥ 90%** (berdasarkan Word Error Rate).  
> - Pipeline lengkap: **Video → Audio → Transkrip → Analisis → JSON HR-friendly**.  
> - Folder `data/samples/` digunakan untuk contoh video dan dataset pengujian.
