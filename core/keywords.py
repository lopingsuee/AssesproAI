import re
def coverage(text, keywords):
    t = " " + re.sub(r"\s+"," ", (text or "").lower()).strip() + " "
    hits = [kw for kw in (keywords or []) if f" {kw.lower()} " in t]
    cov  = len(hits)/max(1, len(keywords or []))
    return hits, cov
