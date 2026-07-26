import os
import json

import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


model = genai.GenerativeModel(
    "gemini-2.5-flash",
    generation_config={
        "response_mime_type": "application/json",
        "temperature": 0.2,
    }
)

def analyze_resume(prompt):

    response = model.generate_content(prompt)

    

    
    try:
        return json.loads(response.text)

    except Exception:
        print(response.text)

        return {
            "ats_score": 0,
            "summary": "Unable to parse AI response.",
            "strengths": [],
            "weaknesses": [],
            "missing_skills": [],
            "recommendations": [],
            "interview_questions": [],
            "raw_response": response.text
        }