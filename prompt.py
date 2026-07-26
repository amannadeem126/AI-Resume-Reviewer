def get_resume_prompt(resume_text):

    return f"""
You are an expert ATS Resume Reviewer.

Analyze this resume.

Return ONLY a JSON object.

Do not explain anything.
Do not add introductory text.
Do not use markdown.
Do not wrap in ```json.
Do not include comments.

The JSON schema MUST be:

{{
    "ats_score": 0,
    "summary": "",
    "strengths": [],
    "weaknesses": [],
    "missing_skills": [],
    "recommendations": [],
    "interview_questions": []
}}

Resume:

{resume_text}
"""