# config.py
import redis
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0

settings = Settings()

redis_client = redis.StrictRedis(
    host=settings.redis_host,
    port=settings.redis_port,
    db=settings.redis_db,
    decode_responses=True  # Para garantir que os dados sejam retornados como strings
)
