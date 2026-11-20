import os
import uuid

from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

from utils.resume_parser import extract_resume_text
from utils.analyzer import analyze_resume, extract_skills


# ==========================================
# APPLICATION CONFIGURATION
# ==========================================

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

ALLOWED_EXTENSIONS = {"pdf"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ==========================================
# HELPER FUNCTION
# ==========================================

def allowed_file(filename):
    return (
        bool(filename)
        and "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


# ==========================================
# HOME API
# ==========================================

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "application": "ResumeIQ",
        "message": "ResumeIQ API is running successfully!",
        "status": "success",
        "version": "1.0.0"
    }), 200


# ==========================================
# HEALTH CHECK API
# ==========================================

@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "healthy",
        "application": "ResumeIQ",
        "message": "Backend server is active."
    }), 200


# ==========================================
# RESUME ANALYSIS API
# ==========================================

@app.route("/api/analyze", methods=["POST"])
def analyze_resume_api():

    file_path = None

    # Check uploaded resume
    if "resume" not in request.files:
        return jsonify({
            "success": False,
            "error": "Please upload your resume PDF."
        }), 400

    resume_file = request.files["resume"]

    # Get job description
    job_description = request.form.get(
        "job_description", ""
    ).strip()

    # Validate uploaded file
    if not resume_file or not resume_file.filename:
        return jsonify({
            "success": False,
            "error": "No resume file selected."
        }), 400

    # Validate PDF extension
    if not allowed_file(resume_file.filename):
        return jsonify({
            "success": False,
            "error": "Invalid file format. Please upload a PDF."
        }), 400

    # Validate job description
    if not job_description:
        return jsonify({
            "success": False,
            "error": "Please enter a job description."
        }), 400

    # Secure filename
    filename = secure_filename(resume_file.filename)

    if not filename:
        return jsonify({
            "success": False,
            "error": "Invalid filename."
        }), 400

    # Generate unique filename
    unique_filename = f"{uuid.uuid4().hex}_{filename}"

    file_path = os.path.join(
        UPLOAD_FOLDER,
        unique_filename
    )

    try:

        # ======================================
        # SAVE UPLOADED PDF
        # ======================================

        resume_file.save(file_path)

        print("\n" + "=" * 55)
        print("RESUMEIQ - NEW RESUME ANALYSIS")
        print("=" * 55)

        print("Uploaded file:", filename)
        print("File size:", os.path.getsize(file_path), "bytes")

        # ======================================
        # EXTRACT RESUME TEXT
        # ======================================

        resume_text = extract_resume_text(file_path)

        print("\n========== PDF EXTRACTION DEBUG ==========")

        print("Extracted characters:", len(resume_text))
        print("Extracted words:", len(resume_text.split()))

        print("\nFirst 2000 characters of extracted text:")

        print(resume_text[:2000])

        print("==========================================")

        # ======================================
        # DETECT SKILLS
        # ======================================

        resume_skills = extract_skills(resume_text)

        job_skills = extract_skills(job_description)

        print("\n========== SKILL DETECTION DEBUG ==========")

        print("Resume skills:", resume_skills)
        print("Job description skills:", job_skills)

        print("Resume skill count:", len(resume_skills))
        print("Job skill count:", len(job_skills))

        print("===========================================")

        # ======================================
        # ANALYZE RESUME
        # ======================================

        analysis_result = analyze_resume(
            resume_text,
            job_description
        )

        print("\n========== ANALYSIS RESULTS ==========")

        print(
            "Resume Match Score:",
            analysis_result["match_score"]
        )

        print(
            "Skill Match Score:",
            analysis_result["skill_match_percentage"]
        )

        print(
            "Matched Skills:",
            analysis_result["matched_skills"]
        )

        print(
            "Missing Skills:",
            analysis_result["missing_skills"]
        )

        print("=====================================\n")

        # ======================================
        # RETURN RESULTS TO FRONTEND
        # ======================================

        return jsonify({
            "success": True,
            "message": "Resume analyzed successfully!",
            "data": analysis_result
        }), 200

    except ValueError as error:

        app.logger.warning(
            "Resume processing error: %s",
            str(error)
        )

        return jsonify({
            "success": False,
            "error": str(error)
        }), 400

    except Exception:

        app.logger.exception(
            "Unexpected resume analysis error"
        )

        return jsonify({
            "success": False,
            "error": "Something went wrong while analyzing your resume."
        }), 500

    finally:

        # ======================================
        # DELETE TEMPORARY PDF
        # ======================================

        if file_path and os.path.exists(file_path):

            try:
                os.remove(file_path)
                print("Temporary PDF deleted.")

            except OSError:
                app.logger.exception(
                    "Unable to delete temporary PDF."
                )


# ==========================================
# FILE SIZE ERROR HANDLER
# ==========================================

@app.errorhandler(413)
def file_too_large(error):
    return jsonify({
        "success": False,
        "error": "Resume file is too large. Maximum allowed size is 5 MB."
    }), 413


# ==========================================
# INVALID ROUTE HANDLER
# ==========================================

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": "Requested API endpoint was not found."
    }), 404


# ==========================================
# START FLASK SERVER
# ==========================================

if __name__ == "__main__":

    print("=" * 55)
    print("             RESUMEIQ BACKEND SERVER")
    print("=" * 55)

    print("Server: http://127.0.0.1:5000")
    print("API: http://127.0.0.1:5000/api/analyze")
    print("Health: http://127.0.0.1:5000/api/health")

    print("=" * 55)

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )