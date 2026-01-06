from fastapi import FastAPI
from app.schemas import JobInput
from app.tasks import generate_questions

app = FastAPI(title="LLM Interview Question Generator")

@app.post("/generate")
def generate(job: JobInput):
    task = generate_questions.delay(
        job.skills,
        job.job_description
    )
    return {"task_id": task.id, "status": "processing"}

@app.get("/status/{task_id}")
def status(task_id: str):
    task = generate_questions.AsyncResult(task_id)
    return {
        "task_id": task_id,
        "status": task.status,
        "result": task.result if task.successful() else None
    }
