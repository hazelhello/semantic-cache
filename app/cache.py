import redis
import numpy as np
from typing import Optional

class SemanticCache:
    def __init__(self, host: str, similarity_threshold: float):
        self.redis = redis.Redis(host=host, port=6379)
        self.threshold = similarity_threshold

    def _cosine_similarity(self, vec1, vec2):
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

    def get(self, text: str) -> Optional[str]:
        query_vec = encode_text(text)
        for key in self.redis.scan_iter("vec:*"):
            cached_vec = np.frombuffer(self.redis.get(key), dtype=np.float32)
            if self._cosine_similarity(query_vec, cached_vec) > self.threshold:
                return self.redis.get(key.decode().replace("vec:", "text:")).decode()
        return None

    def set(self, text: str, response: str):
        vec = encode_text(text)
        self.redis.set(f"vec:{text}", vec.tobytes())
        self.redis.set(f"text:{text}", response)