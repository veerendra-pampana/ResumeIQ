import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==========================================
# SKILLS DATABASE
# ==========================================

SKILLS_DATABASE = {
    "python": ["python", "python programming"],
    "java": ["java", "java programming"],
    "javascript": ["javascript", "js"],
    "typescript": ["typescript", "ts"],
    "c++": ["c++", "cpp"],
    "machine learning": ["machine learning", "ml"],
    "deep learning": ["deep learning", "dl"],
    "artificial intelligence": ["artificial intelligence", "ai"],
    "data science": ["data science"],
    "data analysis": ["data analysis", "data analytics"],
    "data visualization": ["data visualization"],
    "tensorflow": ["tensorflow"],
    "pytorch": ["pytorch"],
    "keras": ["keras"],
    "scikit-learn": ["scikit-learn", "sklearn"],
    "opencv": ["opencv", "open cv"],
    "nlp": ["nlp", "natural language processing"],
    "computer vision": ["computer vision"],
    "html": ["html", "html5"],
    "css": ["css", "css3"],
    "react": ["react", "react.js", "reactjs"],
    "angular": ["angular"],
    "vue": ["vue", "vue.js", "vuejs"],
    "node.js": ["node.js", "nodejs", "node js"],
    "express.js": ["express.js", "expressjs"],
    "flask": ["flask"],
    "django": ["django"],
    "fastapi": ["fastapi", "fast api"],
    "sql": ["sql"],
    "mysql": ["mysql"],
    "postgresql": ["postgresql", "postgres"],
    "mongodb": ["mongodb", "mongo db"],
    "firebase": ["firebase"],
    "git": ["git"],
    "github": ["github", "git hub"],
    "docker": ["docker"],
    "kubernetes": ["kubernetes", "k8s"],
    "aws": ["aws", "amazon web services"],
    "azure": ["azure", "microsoft azure"],
    "google cloud": ["google cloud", "gcp"],
    "linux": ["linux"],
    "rest api": ["rest api", "restful api", "rest apis"],
    "api development": ["api development"],
    "streamlit": ["streamlit"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "matplotlib": ["matplotlib"],
    "seaborn": ["seaborn"],
    "power bi": ["power bi", "powerbi"],
    "tableau": ["tableau"],
    "excel": ["excel", "microsoft excel"],
    "data structures": ["data structures", "dsa"],
    "algorithms": ["algorithms"],
    "object oriented programming": [
        "object oriented programming",
        "oop",
        "oops"
    ],
    "software testing": ["software testing"],
    "manual testing": ["manual testing"],
    "automation testing": ["automation testing"],
    "selenium": ["selenium"],
    "agile": ["agile", "agile methodology"],
    "communication": ["communication", "communication skills"],
    "problem solving": ["problem solving", "problem-solving"],
    "teamwork": ["teamwork", "team work"],
    "leadership": ["leadership"],
    "project management": ["project management"],
    "critical thinking": ["critical thinking"],
    "time management": ["time management"]
}


# ==========================================
# TEXT CLEANING
# ==========================================

def clean_text(text):

    if not isinstance(text, str):
        return ""

    text = text.lower()

    text = text.replace("\n", " ")
    text = text.replace("\t", " ")

    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ==========================================
# SKILL EXTRACTION
# ==========================================

def extract_skills(text):

    cleaned_text = clean_text(text)

    found_skills = []

    for canonical_skill, aliases in SKILLS_DATABASE.items():

        for alias in aliases:

            pattern = (
                r"(?<![a-z0-9])"
                + re.escape(alias.lower())
                + r"(?![a-z0-9])"
            )

            if re.search(pattern, cleaned_text):

                found_skills.append(canonical_skill)
                break

    return sorted(set(found_skills))


# ==========================================
# TEXT SIMILARITY SCORE
# ==========================================

def calculate_match_score(resume_text, job_description):

    resume_text = clean_text(resume_text)
    job_description = clean_text(job_description)

    if not resume_text:
        raise ValueError("Resume text is empty.")

    if not job_description:
        raise ValueError("Job description is empty.")

    try:

        vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2),
            sublinear_tf=True
        )

        vectors = vectorizer.fit_transform([
            resume_text,
            job_description
        ])

        similarity = cosine_similarity(
            vectors[0:1],
            vectors[1:2]
        )[0][0]

        return round(float(similarity) * 100, 2)

    except ValueError as error:

        raise ValueError(
            "Unable to calculate resume similarity. "
            "Please provide more readable resume and job description text."
        ) from error


# ==========================================
# SKILL MATCH CALCULATION
# ==========================================

def calculate_skill_match(resume_skills, job_skills):

    if not job_skills:
        return 0.0

    matched_skills = set(resume_skills).intersection(
        set(job_skills)
    )

    percentage = (
        len(matched_skills) / len(job_skills)
    ) * 100

    return round(percentage, 2)


# ==========================================
# SUGGESTION GENERATOR
# ==========================================

def generate_suggestions(
    resume_text,
    resume_skills,
    job_skills,
    missing_skills,
    match_score
):

    suggestions = []

    word_count = len(resume_text.split())

    if word_count < 100:

        suggestions.append(
            "Your resume contains limited readable text. "
            "Add details about your education, projects, "
            "internships and experience."
        )

    if not resume_skills:

        suggestions.append(
            "No recognized skills were detected in your resume. "
            "Check whether your PDF contains selectable text "
            "and clearly mention your technical skills."
        )

    if not job_skills:

        suggestions.append(
            "No recognized skills were detected in the job description. "
            "Include specific technical requirements for better comparison."
        )

    if missing_skills:

        suggestions.append(
            "Consider developing or highlighting these job-related skills: "
            + ", ".join(missing_skills)
        )

    if match_score < 30:

        suggestions.append(
            "Your resume has relatively low textual similarity "
            "with the job description. Include relevant experience "
            "and project details where accurate."
        )

    elif match_score < 60:

        suggestions.append(
            "Improve your resume by emphasizing relevant experience, "
            "technical skills and measurable project achievements."
        )

    else:

        suggestions.append(
            "Your resume has good textual relevance. "
            "Strengthen it further with measurable achievements."
        )

    return suggestions


# ==========================================
# MAIN RESUME ANALYSIS
# ==========================================

def analyze_resume(resume_text, job_description):

    if not isinstance(resume_text, str) or not resume_text.strip():

        raise ValueError(
            "Resume text cannot be empty. "
            "Please upload a readable PDF."
        )

    if not isinstance(job_description, str) or not job_description.strip():

        raise ValueError(
            "Job description cannot be empty."
        )

    # Clean both inputs
    cleaned_resume = clean_text(resume_text)
    cleaned_job = clean_text(job_description)

    # Extract skills
    resume_skills = extract_skills(cleaned_resume)
    job_skills = extract_skills(cleaned_job)

    # Find matching skills
    matched_skills = sorted(
        set(resume_skills).intersection(set(job_skills))
    )

    # Find missing skills
    missing_skills = sorted(
        set(job_skills) - set(resume_skills)
    )

    # Calculate resume similarity
    match_score = calculate_match_score(
        cleaned_resume,
        cleaned_job
    )

    # Calculate skill match
    skill_match_percentage = calculate_skill_match(
        resume_skills,
        job_skills
    )

    # Generate suggestions
    suggestions = generate_suggestions(
        cleaned_resume,
        resume_skills,
        job_skills,
        missing_skills,
        match_score
    )

    # Return analysis results
    return {
        "match_score": match_score,
        "skill_match_percentage": skill_match_percentage,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "suggestions": suggestions
    }