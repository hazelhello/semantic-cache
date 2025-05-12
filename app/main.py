from fastapi import FastAPI
from pydantic import BaseModel
from model import encode_text  # 自定义SBERT编码函数
from cache import SemanticCache

app = FastAPI()
cache = SemanticCache(host="redis", similarity_threshold=0.85)

class QueryRequest(BaseModel):
    text: str

@app.post("/query")
async def query(request: QueryRequest):
    # 1. 检查语义缓存
    cached_response = cache.get(request.text)
    if cached_response:
        return {"result": cached_response, "source": "cache"}

    # 2. 模拟调用大模型（未命中缓存时）
    llm_response = f"这是对'{request.text}'的生成结果"  # 替换为真实API调用
    cache.set(request.text, llm_response)  # 存入缓存
    return {"result": llm_response, "source": "llm"}