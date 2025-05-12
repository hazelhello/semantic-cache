from sentence_transformers import SentenceTransformer
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def encode_text(text: str):
    return model.encode(text)  # 返回768维向量