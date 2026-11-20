# ResumeIQ
ResumeIQ – An AI-powered Resume Analyzer built with React, Flask, Python, and NLP techniques to evaluate resumes against job descriptions, calculate match scores, identify skill gaps, and provide improvement suggestions.
# ResumeIQ – AI-Powered Resume Analyzer

ResumeIQ is an intelligent resume analysis application that helps job seekers evaluate how well their resumes match specific job descriptions.

The application analyzes uploaded PDF resumes, extracts relevant information, identifies matching and missing skills, calculates compatibility scores, and provides suggestions to improve resume relevance.

Built using **React, Flask, Python, and NLP techniques**, ResumeIQ provides a simple and interactive platform for resume evaluation.

## 🚀 Features

- **Resume Upload:** Upload your resume in PDF format.
- **Job Description Analysis:** Enter a job description to evaluate your resume against a target role.
- **Resume Parsing:** Extract text from PDF resumes using Python.
- **Skill Extraction:** Identify relevant technical skills from resumes and job descriptions.
- **Match Score:** Calculate an overall resume-to-job-description compatibility score.
- **Skill Match Percentage:** View how many required skills match your resume.
- **Matched Skills:** Identify skills already present in your resume.
- **Missing Skills:** Discover skills that may need improvement.
- **Improvement Suggestions:** Receive suggestions to improve your resume.

## 🛠️ Tech Stack

### Frontend
- React.js
- Vite
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask
- Flask-CORS

### Machine Learning & NLP
- Scikit-learn
- TF-IDF
- Text Processing
- Rule-based Skill Extraction

### PDF Processing
- PyMuPDF

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── backend/
│   ├── uploads/
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── analyzer.py
│   │   └── resume_parser.py
│   ├── app.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

Follow these steps to run ResumeIQ locally.

### 1. Clone the Repository

```bash
git clone https://github.com/veerendra-pampana/ResumeIQ.git
```

```bash
cd ResumeIQ
```

### 2. Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Start the Flask backend:

```bash
python app.py
```

The backend will run at:

`http://127.0.0.1:5000`

### 3. Frontend Setup

Open another terminal and navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the React development server:

```bash
npm run dev
```

Open the frontend in your browser:

`http://localhost:5173`

## 🔄 Application Workflow

1. Launch the ResumeIQ application.
2. Upload a resume in PDF format.
3. Enter the target job description.
4. Submit the information for analysis.
5. The backend extracts resume text and analyzes relevant skills.
6. The application calculates compatibility scores.
7. View matched skills, missing skills, and improvement suggestions.

## 📊 Analysis Results

ResumeIQ provides the following results:

| Result | Description |
|---|---|
| Match Score | Overall resume and job description compatibility |
| Skill Match | Percentage of identified job skills found in the resume |
| Matched Skills | Skills detected in both the resume and job description |
| Missing Skills | Job-related skills not detected in the resume |
| Suggestions | Recommendations for improving resume relevance |

## 🎯 Project Objective

The main objective of ResumeIQ is to simplify resume evaluation and help job seekers understand how closely their qualifications align with job requirements.

It aims to make resume improvement more accessible by highlighting skill gaps and providing actionable feedback.

## 🔮 Future Enhancements

- Integration with advanced AI language models.
- Support for additional resume formats.
- More advanced semantic skill matching.
- Resume improvement recommendations.
- Resume scoring and analysis history.
- Downloadable analysis reports.

## 👨‍💻 Developer

**Veerendra Pampana**

- GitHub: https://github.com/veerendra-pampana
- LinkedIn: https://www.linkedin.com/in/veerendra-pampana-34aa66256/
- Portfolio: https://veerendra-portfolio-eight.vercel.app

## 📄 License

This project is available for educational and personal learning purposes.
