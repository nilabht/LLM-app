from app.celery_app import celery_app
from app.llm import call_llm
from app.schemas import QuestionList

@celery_app.task(
    bind=True,
    autoretry_for=(Exception,),
    retry_kwargs={"max_retries": 3, "countdown": 5}
)
def generate_questions(self, skills, job_description):
    raw_output = call_llm(skills, job_description)
    validated = QuestionList.model_validate(raw_output)
    return validated.model_dump()