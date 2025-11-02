def structure_score(text: str) -> float:
    t = (text or "").lower()
    intro = any(p in t for p in ["perkenalkan","nama saya","i am","my name"])
    body  = len(t.split()) >= 60
    close = any(p in t for p in ["motivasi","tertarik","value","nilai","kontribusi"])
    return 1.0 if (intro and body and close) else 0.0