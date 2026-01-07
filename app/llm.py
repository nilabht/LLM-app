from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from app.config import OPENAI_API_KEY, OPENAI_MODEL
import json

llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model=OPENAI_MODEL,
    temperature=0
)

prompt_template = PromptTemplate(
    input_variables=["skills", "job_description"],
    template="""
You are a senior AI recruiter.

Job Description:
{job_description}

Skills:
{skills}

TASK:
Generate exactly 10 interview questions.

Rules:
- Output must be a JSON array
- Each object must contain:
  - question
  - question_type (normal or knockout)
  - answer_prompting
- At least 3 questions must be knockout
- Knockout questions must disqualify candidates
- Answer prompting must be short (yes/no, years, brief explanation)

Return ONLY valid JSON. No markdown. No explanation.
"""
)

def call_llm(skills, job_description):
    prompt = prompt_template.format(
        skills=", ".join(skills),
        job_description=job_description
    )

    response = llm.invoke(prompt)

    return json.loads(response.content)
