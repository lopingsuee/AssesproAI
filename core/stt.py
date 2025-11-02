def _whisper(wav_path, cfg):
    import whisper
    model = whisper.load_model(cfg["models"]["whisper_size"])
    result = model.transcribe(str(wav_path), language="id", word_timestamps=False)
    text = (result.get("text") or "").strip()
    segs = result.get("segments", [])
    if segs:
        avg_logprob = sum(s.get("avg_logprob",-1.0) for s in segs)/len(segs)
        ns_prob = sum(s.get("no_speech_prob",0.0) for s in segs)/len(segs)
        dur = float(segs[-1]["end"] - segs[0]["start"])
    else:
        avg_logprob, ns_prob, dur = -2.0, 1.0, 0.0
    return text, segs, {"avg_logprob": avg_logprob, "no_speech_prob": ns_prob, "duration_sec": dur}

import os
import json
import whisper

def transcribe(wav_path, cfg):
    model = whisper.load_model(cfg["models"]["whisper_size"])
    result = model.transcribe(str(wav_path), language="en")

    text = result["text"]
    segments = result["segments"]
    meta = {
        "avg_logprob": result["segments"][0]["avg_logprob"],
        "no_speech_prob": result["segments"][0]["no_speech_prob"],
        "duration_sec": result["segments"][-1]["end"]
    }

    # 🆕 Auto-save hasil transkripsi ke tmp/transcripts/
    os.makedirs("tmp/transcripts", exist_ok=True)
    base = os.path.splitext(os.path.basename(wav_path))[0]
    out_path = f"tmp/transcripts/{base}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({"text": text, "meta": meta}, f, ensure_ascii=False, indent=2)

    print(f"✅ Transkrip disimpan ke: {out_path}")

    return text, segments, meta
