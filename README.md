# Resume Analyzer

A basic beginner level AI-powered web app that analyzes a candidate's resume and recommends the most suitable job role based on their skills, education, and experience.

## Features

- Upload a resume in PDF or DOCX format
- Automatic text extraction from the uploaded file
- AI-powered analysis using an LLM (via Groq API):
  - Identifies technical and soft skills
  - Summarizes the candidate's profile
  - Recommends the most suitable job role
  - Highlights missing skills for the recommended role
- Clean, organized dashboard-style results

## Tech Stack

- **Python**
- **Streamlit** – web app interface
- **Groq API** – LLM-powered resume analysis
- **pdfplumber** – PDF text extraction
- **python-docx** – DOCX text extraction

## How It Works

1. Upload a resume (PDF or DOCX)
2. The app extracts and cleans the text from the file
3. The extracted text is sent to an LLM with a structured prompt
4. The LLM returns skills, a profile summary, a recommended role, and missing skills as JSON
5. Results are displayed in a readable dashboard layout

## Setup

1. Clone this repository
   ```bash
   git clone  https://github.com/kusijain/Resume_analyzer.git
   cd resume-analyzer
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Groq API key
   ```
   GROQ_API_KEY=your_key_here
   ```
   Get a free API key at [console.groq.com](https://console.groq.com)

4. Run the app
   ```bash
   streamlit run app.py
   ```

## Live Demo

(https://resumeanalyzer-7wbrrhthrftmutbdmq7srm.streamlit.app/)

## Notes

This project was built as a learning exercise to explore LLM-powered applications, resume parsing, and Streamlit dashboard design.
