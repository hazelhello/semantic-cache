一个基于语义相似度的轻量级缓存服务，通过AI模型识别相似问题，减少对大语言模型(LLM)的重复调用，显著降低API成本并提升响应速度。

#本地运行

# 安装依赖
pip install -r requirements.txt  # fastapi, redis, sentence-transformers, numpy

# 启动Redis（需Docker）
docker run -p 6379:6379 redis

# 启动服务
uvicorn app.main:app --reload


#API测试

curl -X POST "http://127.0.0.1:8000/query" \
-H "Content-Type: application/json" \
-d '{"text":"如何学习机器学习？"}'

# 响应示例
{"result":"这是对'如何学习机器学习？'的生成结果","source":"llm"}

# 第二次请求相同/相似问题会命中缓存
{"result":"这是对'如何学习机器学习？'的生成结果","source":"cache"}
