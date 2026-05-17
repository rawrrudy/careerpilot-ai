from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input structure
class StudentData(BaseModel):
    interests: list[str]
    skills: list[str]
    grade: int

# Home route
@app.get("/")
def home():
    return {"message": "CareerPilot Backend Running"}

# Career recommendation route
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

    Keep the response concise and beginner-friendly.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert AI career guidance counselor."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    text = response.choices[0].message.content.replace("**", "")

    return {
        "recommendation": response.choices[0].message.content
    }