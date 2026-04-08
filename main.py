# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import google.genai as genai
from config import API_KEY  # import API key from config.py

# 🔧 Configure AI
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

# 🚀 FastAPI app instance
app = FastAPI()

# 🔹 Test route
@app.get("/")
def home():
    return {"message": "Backend is working 🚀"}

# 🔹 Input model for POST requests
class Answer(BaseModel):
    text: str

# 🔹 AI feedback function
def get_ai_feedback(answer_text):
    prompt = f"""
You are a strict but helpful teacher.

Analyze this student answer and give:
1. Mistakes
2. Suggestions
3. Score out of 10

Answer: {answer_text}
"""
    response = model.generate_content(prompt)
    return response.text

# 🔹 Submit-answer API endpoint
@app.post("/submit-answer")
def submit_answer(answer: Answer):
    feedback = get_ai_feedback(answer.text)
    return {"feedback": feedback}
