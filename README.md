# ATS Resume Expert

This project is an **AI-powered Applicant Tracking System (ATS) Resume Analyzer** that helps job seekers evaluate their resumes against job descriptions using Google Gemini AI. It provides insights into resume strengths, improvement areas, and an ATS match percentage.

## Features
- **Resume Review:** Evaluates a resume against a job description and highlights strengths & weaknesses.
- **Skill Enhancement Advice:** Provides career growth recommendations and a roadmap for skill improvement.
- **ATS Score Calculation:** Computes a **percentage match** between the resume and job description, lists missing keywords, and gives final feedback.

## Technologies Used
- **Streamlit** (Web UI Framework)
- **Google Gemini AI** (AI-based resume evaluation)
- **pdf2image** (Extracts images from PDF resumes)
- **PIL (Pillow)** (Processes images)
- **Base64 & IO** (Handles PDF image encoding)

## Installation
Install the required dependencies:
```bash
pip install streamlit pdf2image pillow google-generativeai python-dotenv
```

## Usage
1. Clone the repository:
```bash
git clone https://github.com/yourusername/ATS-Resume-Expert.git
cd ATS-Resume-Expert
```
2. Set up your **Google API Key** in a `.env` file:
```env
GOOGLE_API_KEY=your_api_key_here
```
3. Run the Streamlit application:
```bash
streamlit run app.py
```
4. Upload your resume (PDF format) and enter the job description.
5. Click buttons to analyze the resume, get skill improvement suggestions, or calculate ATS match percentage.

## Example Output
- **Resume Analysis:**
  - "Your resume aligns well with the role, but you should emphasize skills in Python and SQL."
- **Skill Improvement:**
  - "To increase your chances, learn Kubernetes and cloud platforms like AWS."
- **ATS Score:**
  - "Match Percentage: 85% | Missing Keywords: TensorFlow, Flask | Final Thoughts: Consider adding relevant projects."

## Contributing
Feel free to submit issues or pull requests to enhance this project.


