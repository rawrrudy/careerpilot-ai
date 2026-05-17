from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()


# Input structure
class StudentData(BaseModel):
    interests: list[str]
    skills: list[str]
    grade: int


@app.get("/")
def home():
    return {"message": "CareerPilot Backend Running"}


@app.post("/career-recommendation")
def recommend_career(data: StudentData):

    prompt = f"""
    A student in grade {data.grade}
    has interests in {data.interests}
    and skills in {data.skills}.

    Suggest:
    1. Best career option
    2. Why it suits them
    3. Skills they should learn next

    Keep response concise.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a career guidance AI."},
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "recommendation": response.choices[0].message.content
    }