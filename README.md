# AssesproAI
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
