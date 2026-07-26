# 🤖 AI Resume Reviewer

An AI-powered Resume Reviewer built with **Python**, **Streamlit**, and **Google Gemini** that analyzes PDF resumes, evaluates ATS compatibility, identifies strengths and weaknesses, detects missing skills, and provides personalized recommendations for improving job applications.

---

## 🚀 Live Demo

🔗 https://ai-resume-reviewer126.streamlit.app

---

## 📌 Features

- 📄 Upload Resume (PDF)
- 🤖 AI-powered Resume Analysis using Google Gemini
- 🎯 ATS Compatibility Score
- 💪 Resume Strengths Identification
- ⚠️ Weaknesses Detection
- 🧠 Missing Skills Recommendation
- 🚀 Personalized Improvement Suggestions
- 🎤 AI-generated Interview Questions
- 📊 Resume Statistics (Word Count & Character Count)
- 🎨 Modern and Responsive Streamlit Interface

---

## 🛠️ Tech Stack

### Frontend
- Streamlit
- HTML
- CSS

### Backend
- Python

### AI
- Google Gemini 2.5 Flash API
- Prompt Engineering

### Libraries
- PyPDF2
- python-dotenv
- google-generativeai
- Streamlit

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```text
AI-Resume-Reviewer/
│
├── app.py
├── ai.py
├── parser.py
├── prompt.py
├── utils.py
├── style.css
├── requirements.txt
├── .gitignore
├── README.md
└── .env (not included)
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/amannadeem126/AI-Resume-Reviewer.git
```

Go into the project directory

```bash
cd AI-Resume-Reviewer
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

You can obtain a Gemini API key from:

https://aistudio.google.com/app/apikey

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---


## 📈 What the AI Evaluates

The application analyzes resumes for:

- ATS Compatibility
- Resume Summary
- Technical Skills
- Missing Skills
- Strengths
- Weaknesses
- Resume Improvements
- Interview Preparation Questions

---

## 🎯 Future Improvements

- Resume Keyword Optimization
- Multiple Resume Templates
- Resume vs Job Description Matching
- Download AI Report as PDF
- Resume Score History
- Multi-language Support
- Authentication System

---

## 👨‍💻 Author

**Aman Nadeem**

Software Engineering Student

GitHub:
https://github.com/amannadeem126

LinkedIn:
https://www.linkedin.com/in/aman-nadeem-70335726a

---

## ⭐ If you like this project

Please consider giving this repository a ⭐ on GitHub.

It helps support the project and motivates future improvements.