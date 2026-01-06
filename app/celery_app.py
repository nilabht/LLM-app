from celery import Celery
from app.config import REDIS_BROKER_URL, REDIS_RESULT_BACKEND
celery_app = Celery(
    "llm_tasks",
    broker=REDIS_BROKER_URL,
    backend=REDIS_RESULT_BACKEND,
)
import app.tasks