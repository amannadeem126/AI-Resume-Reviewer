import os
import json

import google.generativeai as genai
from dotenv import load_dotenv
print("AI.PY LOADED")
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_resume(prompt):

    response = model.generate_content(prompt)

    print("\n" + "=" * 100)
    print("RAW GEMINI RESPONSE:")
    print(response.text)
    print("=" * 100 + "\n")

    text = response.text.strip()

    # Remove markdown if Gemini ever returns it
    text = text.replace("```json", "")
    text = text.replace("```", "").strip()

    try:
        return json.loads(text)

    except Exception:

        return {
            "ats_score": 0,
            "summary": "Unable to parse AI response.",
            "strengths": [],
            "weaknesses": [],
            "missing_skills": [],
            "recommendations": [],
            "interview_questions": [],
            "raw_response": text
        }