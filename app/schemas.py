from pydantic import BaseModel, Field, RootModel
from typing import List, Literal

class JobInput(BaseModel):
    skills: List[str] = Field(..., min_items=1)
    job_description: str = Field(..., min_length=20)

class Question(BaseModel):
    question: str
    question_type: Literal["normal", "knockout"]
    answer_prompting: str

class QuestionList(RootModel[List[Question]]):
    pass
