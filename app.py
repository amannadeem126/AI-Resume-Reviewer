import ai

print("USING AI FILE:", ai.__file__)

import streamlit as st
import streamlit as st
from parser import extract_text_from_pdf
from ai import analyze_resume
from prompt import get_resume_prompt
from utils import (
    count_words,
    count_characters,
    get_filename
)
def load_css():

    with open("style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


# Configure the page
st.set_page_config(
    page_title="AI Resume Reviewer",
    page_icon="📄",
    layout="wide"
)
load_css()
st.markdown("""
<div class="hero-card">

<h1>🤖 AI Resume Reviewer</h1>

<h4>Professional AI-powered Resume Analysis using Google Gemini</h4>

<p>
Upload your resume and receive detailed ATS feedback,
missing skills,
career suggestions,
interview questions,
and personalized improvements.
</p>

</div>
""", unsafe_allow_html=True)
# File uploader
uploaded_file = st.file_uploader(
    "Choose your resume (PDF only)",
    type=["pdf"]
)
# Check if a file is uploaded
if uploaded_file is not None:

    st.success("✅ Resume uploaded successfully!")
    st.write(f"Filename: {uploaded_file.name}")

    # Extract text
    resume_text = extract_text_from_pdf(uploaded_file)
    resume_text = resume_text[:6000]
    filename = get_filename(uploaded_file)
    word_count = count_words(resume_text)
    character_count = count_characters(resume_text)

    # Analyze with AI
    progress = st.progress(0)

    for i in range(100):
        progress.progress(i + 1)
    with st.spinner("🤖 Gemini is analyzing your resume..."):
        prompt = get_resume_prompt(resume_text)
        ai_response = analyze_resume(prompt)
    score = ai_response.get("ats_score", 0)
    progress.empty()

# Extract values from JSON
    score = ai_response.get("ats_score", 0)
    summary = ai_response.get("summary", "")
    strengths = ai_response.get("strengths", [])
    weaknesses = ai_response.get("weaknesses", [])
    missing_skills = ai_response.get("missing_skills", [])
    recommendations = ai_response.get("recommendations", [])
    interview_questions = ai_response.get("interview_questions", [])
# Show extracted text
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
        "📄 File",
        filename
    )
    with col2:
        st.metric(
        "📝 Words",
        word_count
    )
    with col3:
        st.metric(
        "🔠 Characters",
        character_count
    )
    # -------------------------------
# ATS Score
# -------------------------------

    st.divider()

    st.subheader("🎯 ATS Score")

    st.progress(score / 100)

    st.metric(
        "Overall ATS Score",
        f"{score}/100"
)
# -------------------------------
# Summary
# -------------------------------

    st.divider()

    st.subheader("📄 Professional Summary")

    st.info(summary)

# -------------------------------
# Strengths
# -------------------------------

    st.divider()

    st.subheader("💪 Strengths")

    for item in strengths:
        st.success(f"✅ {item}")

# -------------------------------
# Weaknesses
# -------------------------------

    st.divider()

    st.subheader("⚠ Weaknesses")

    for item in weaknesses:
        st.warning(f"⚠ {item}")

# -------------------------------
# Missing Skills
# -------------------------------

    st.divider()

    st.subheader("🧠 Missing Skills")

    cols = st.columns(3)

    for index, skill in enumerate(missing_skills):

        cols[index % 3].markdown(
            f"""
<div style="
padding:10px;
border-radius:12px;
background:#EEF2FF;
text-align:center;
font-weight:600;
margin-bottom:10px;
">
{skill}
</div>
""",
        unsafe_allow_html=True,
    )
# -------------------------------
# Recommendations
# -------------------------------

    st.divider()

    st.subheader("🚀 Recommendations")

    for item in recommendations:
        st.info(f"💡 {item}")

# -------------------------------
# Interview Questions
# -------------------------------

    st.divider()

    with st.expander("🎤 Interview Questions"):

        for i, question in enumerate(interview_questions, 1):
            st.write(f"**{i}.** {question}")

# -------------------------------
# Resume Preview
# -------------------------------

    st.divider()

    with st.expander("📄 View Extracted Resume", expanded=False):
        st.text_area(
        "",
        resume_text,
        height=350
    )
