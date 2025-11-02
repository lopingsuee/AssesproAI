def detect_language(text: str):
    from langdetect import detect, DetectorFactory
    DetectorFactory.seed = 42
    try:
        lang = detect(text) if len(text) >= 20 else "id"
        conf = 0.6
    except:
        lang, conf = "unknown", 0.0
    return {"lang": lang, "confidence": conf}
