from sentence_transformers import SentenceTransformer, util
_models = {}

def _get(model_name):
    if model_name not in _models:
        _models[model_name] = SentenceTransformer(model_name)
    return _models[model_name]

def sbert_similarity(a: str, b: str, model_name: str) -> float:
    m = _get(model_name)
    ea = m.encode(a, convert_to_tensor=True, normalize_embeddings=True)
    eb = m.encode(b, convert_to_tensor=True, normalize_embeddings=True)
    return float(util.cos_sim(ea, eb))