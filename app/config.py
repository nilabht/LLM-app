import os

REDIS_BROKER_URL = os.getenv("REDIS_BROKER_URL", "redis://redis:6379/0")
REDIS_RESULT_BACKEND = os.getenv("REDIS_RESULT_BACKEND", "redis://redis:6379/1")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-4o-mini"