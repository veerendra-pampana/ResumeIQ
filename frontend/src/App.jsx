import { useState } from 'react'
import {
  FileText,
  UploadCloud,
  BrainCircuit,
  Target,
  Sparkles,
  CheckCircle2,
  ArrowRight,
  ShieldCheck,
  Zap,
  BarChart3,
  X,
  FileCheck2,
  Menu,
  LayoutDashboard,
  History,
  Settings,
  LoaderCircle,
  AlertCircle,
} from 'lucide-react'

import './App.css'

const API_URL = 'http://127.0.0.1:5000/api/analyze'

function App() {
  const [file, setFile] = useState(null)
  const [jobDescription, setJobDescription] = useState('')
  const [loading, setLoading] = useState(false)
  const [menuOpen, setMenuOpen] = useState(false)
  const [results, setResults] = useState(null)
  const [error, setError] = useState('')

  // ==========================================
  // FILE UPLOAD
  // ==========================================

  const handleFile = (event) => {
    const selectedFile = event.target.files?.[0]

    if (!selectedFile) return

    if (
      selectedFile.type !== 'application/pdf' &&
      !selectedFile.name.toLowerCase().endsWith('.pdf')
    ) {
      setError('Please upload a PDF resume.')
      event.target.value = ''
      return
    }

    if (selectedFile.size > 5 * 1024 * 1024) {
      setError('Resume file must be smaller than 5 MB.')
      event.target.value = ''
      return
    }

    setFile(selectedFile)
    setError('')
    setResults(null)
  }

  // ==========================================
  // REMOVE SELECTED FILE
  // ==========================================

  const removeFile = (event) => {
    event.preventDefault()
    event.stopPropagation()

    setFile(null)
    setResults(null)
    setError('')

    const input = document.getElementById('resume-upload')

    if (input) input.value = ''
  }

  // ==========================================
  // RESUME ANALYSIS API
  // ==========================================

  const handleAnalyze = async () => {
    setError('')
    setResults(null)

    if (!file) {
      setError('Please upload your resume first.')
      return
    }

    if (!jobDescription.trim()) {
      setError('Please enter a job description.')
      return
    }

    const formData = new FormData()

    formData.append('resume', file)
    formData.append('job_description', jobDescription)

    try {
      setLoading(true)

      const response = await fetch(API_URL, {
        method: 'POST',
        body: formData,
      })

      const responseData = await response.json()

      if (!response.ok) {
        throw new Error(
          responseData.error || 'Resume analysis failed.'
        )
      }

      if (!responseData.success || !responseData.data) {
        throw new Error('Invalid response received from the server.')
      }

      setResults(responseData.data)

    } catch (err) {
      console.error('Resume analysis error:', err)

      setError(
        err.message ||
        'Unable to connect to the backend. Make sure Flask is running.'
      )

    } finally {
      setLoading(false)
    }
  }

  // ==========================================
  // MAIN APPLICATION
  // ==========================================

  return (
    <div className="app-container">

      {/* SIDEBAR */}

      <aside className={`sidebar ${menuOpen ? 'sidebar-open' : ''}`}>

        <div className="brand">
          <div className="brand-icon">
            <BrainCircuit size={25} />
          </div>

          <span>
            Resume<span className="brand-highlight">IQ</span>
          </span>
        </div>

        <div className="workspace-label">WORKSPACE</div>

        <nav className="sidebar-nav">

          <a href="#dashboard" className="nav-item active">
            <LayoutDashboard size={19} />
            <span>Dashboard</span>
          </a>

          <a href="#results" className="nav-item">
            <History size={19} />
            <span>Analysis Results</span>
          </a>

          <a href="#settings" className="nav-item">
            <Settings size={19} />
            <span>Settings</span>
          </a>

        </nav>

        <div className="sidebar-bottom">

          <div className="upgrade-card">

            <div className="upgrade-icon">
              <Sparkles size={20} />
            </div>

            <h3>Unlock your potential</h3>

            <p>
              Make your resume stand out with intelligent insights.
            </p>

            <button className="upgrade-button">
              Explore features <ArrowRight size={15} />
            </button>

          </div>

          <div className="user-profile">

            <div className="avatar">V</div>

            <div>
              <h4>Veerendra</h4>
              <p>Free Account</p>
            </div>

          </div>

        </div>

      </aside>

      {/* MAIN CONTENT */}

      <main className="main-content" id="dashboard">

        {/* TOPBAR */}

        <header className="topbar">

          <button
            className="mobile-menu"
            onClick={() => setMenuOpen(!menuOpen)}
          >
            <Menu size={23} />
          </button>

          <div className="breadcrumb">
            Workspace <span>/</span> <strong>Dashboard</strong>
          </div>

          <div className="topbar-right">

            <div className="status-indicator">
              <span></span> Backend Connected
            </div>

            <div className="top-avatar">V</div>

          </div>

        </header>

        {/* DASHBOARD */}

        <div className="dashboard-content">

          {/* WELCOME */}

          <section className="welcome-section">

            <div>

              <div className="welcome-tag">
                <Sparkles size={14} />
                AI-POWERED CAREER ASSISTANT
              </div>

              <h1>
                Build a resume that <span>gets noticed.</span>
              </h1>

              <p>
                Analyze your resume, discover missing skills, and improve
                your chances of landing your dream job.
              </p>

            </div>

            <div className="welcome-illustration">

              <div className="illustration-circle">

                <FileCheck2 size={65} />

                <div className="floating-star star-one">✦</div>
                <div className="floating-star star-two">✧</div>

              </div>

            </div>

          </section>

          {/* STATISTICS */}

          <section className="stats-grid">

            <div className="stat-card">

              <div className="stat-icon purple">
                <FileText size={21} />
              </div>

              <div>
                <p>Resume Analysis</p>
                <h2>Smart Analysis</h2>
                <span>Detailed resume insights</span>
              </div>

            </div>

            <div className="stat-card">

              <div className="stat-icon blue">
                <Target size={21} />
              </div>

              <div>
                <p>Job Matching</p>
                <h2>Skill Match</h2>
                <span>Compare job requirements</span>
              </div>

            </div>

            <div className="stat-card">

              <div className="stat-icon green">
                <Zap size={21} />
              </div>

              <div>
                <p>Instant Feedback</p>
                <h2>Actionable</h2>
                <span>Improve your resume</span>
              </div>

            </div>

          </section>

          {/* ANALYSIS FORM */}

          <section className="analysis-section">

            <div className="section-heading">

              <div>
                <h2>Start a new analysis</h2>
                <p>
                  Upload your resume and add your target job description.
                </p>
              </div>

              <div className="secure-badge">
                <ShieldCheck size={15} />
                Secure Upload
              </div>

            </div>

            <div className="analysis-grid">

              {/* RESUME UPLOAD */}

              <div className="form-card">

                <div className="card-heading">

                  <div className="step-number">01</div>

                  <div>
                    <h3>Upload your resume</h3>
                    <p>Choose your latest resume in PDF format.</p>
                  </div>

                </div>

                <label className="upload-area" htmlFor="resume-upload">

                  <input
                    id="resume-upload"
                    type="file"
                    accept=".pdf,application/pdf"
                    onChange={handleFile}
                    hidden
                  />

                  {file ? (

                    <div className="selected-file">

                      <div className="file-icon">
                        <FileCheck2 size={30} />
                      </div>

                      <h4>{file.name}</h4>

                      <p>
                        {(file.size / 1024).toFixed(1)} KB
                      </p>

                      <span className="file-success">
                        <CheckCircle2 size={15} />
                        File selected
                      </span>

                      <button
                        type="button"
                        className="remove-file"
                        onClick={removeFile}
                      >
                        <X size={16} />
                      </button>

                    </div>

                  ) : (

                    <>

                      <div className="upload-icon">
                        <UploadCloud size={34} />
                      </div>

                      <h4>Drop your resume here</h4>

                      <p>
                        or <span>browse files</span> from your computer
                      </p>

                      <div className="file-format">
                        <FileText size={14} />
                        PDF FORMAT ONLY
                      </div>

                    </>

                  )}

                </label>

                <div className="upload-note">
                  <ShieldCheck size={15} />
                  Your resume is handled securely.
                </div>

              </div>

              {/* JOB DESCRIPTION */}

              <div className="form-card">

                <div className="card-heading">

                  <div className="step-number">02</div>

                  <div>
                    <h3>Target job description</h3>
                    <p>
                      Paste the job requirements you want to match.
                    </p>
                  </div>

                </div>

                <textarea
                  className="job-textarea"
                  placeholder={`Paste your target job description here...

Example:
We are looking for a Python Developer with knowledge of Machine Learning, Flask, SQL and problem-solving skills...`}
                  value={jobDescription}
                  onChange={(event) => {
                    setJobDescription(event.target.value)
                    setError('')
                    setResults(null)
                  }}
                />

                <div className="textarea-footer">
                  <span>{jobDescription.length} characters</span>
                  <span>Job requirements</span>
                </div>

              </div>

            </div>

            {/* ERROR MESSAGE */}

            {error && (

              <div className="error-message">
                <AlertCircle size={18} />
                <span>{error}</span>
              </div>

            )}

            {/* ANALYZE BUTTON */}

            <div className="analyze-container">

              <button
                className="analyze-button"
                onClick={handleAnalyze}
                disabled={loading}
              >

                {loading ? (
                  <>
                    <LoaderCircle className="spin" size={19} />
                    Analyzing Resume...
                  </>
                ) : (
                  <>
                    <Sparkles size={19} />
                    Analyze My Resume
                    <ArrowRight size={19} />
                  </>
                )}

              </button>

              <p>
                <ShieldCheck size={14} />
                Powered by intelligent resume analysis
              </p>

            </div>

          </section>

          {/* ANALYSIS RESULTS */}

          {results && (

            <section className="results-section" id="results">

              <div className="section-heading">
                <div>
                  <h2>Your analysis results</h2>
                  <p>
                    Here's how your resume matches the target job.
                  </p>
                </div>

                <div className="secure-badge">
                  <CheckCircle2 size={15} />
                  Analysis Complete
                </div>
              </div>

              {/* MATCH SCORES */}

              <div className="results-grid">

                <div className="result-card">

                  <div className="result-icon purple">
                    <BarChart3 size={23} />
                  </div>

                  <p>Resume Match Score</p>

                  <h2>
                    {Number(results.match_score || 0).toFixed(2)}%
                  </h2>

                  <span>Overall text similarity</span>

                </div>

                <div className="result-card">

                  <div className="result-icon green">
                    <Target size={23} />
                  </div>

                  <p>Skill Match</p>

                  <h2>
                    {Number(
                      results.skill_match_percentage || 0
                    ).toFixed(2)}%
                  </h2>

                  <span>Required skills matched</span>

                </div>

              </div>

              {/* MATCHED SKILLS */}

              <div className="skills-result-card">

                <h3>
                  <CheckCircle2 size={19} />
                  Matched Skills
                </h3>

                <div className="skills-list">

                  {results.matched_skills?.length > 0 ? (

                    results.matched_skills.map((skill) => (
                      <span className="skill-tag matched" key={skill}>
                        {skill}
                      </span>
                    ))

                  ) : (

                    <p>No matching skills detected.</p>

                  )}

                </div>

              </div>

              {/* MISSING SKILLS */}

              <div className="skills-result-card">

                <h3>
                  <Target size={19} />
                  Missing Skills
                </h3>

                <div className="skills-list">

                  {results.missing_skills?.length > 0 ? (

                    results.missing_skills.map((skill) => (
                      <span className="skill-tag missing" key={skill}>
                        {skill}
                      </span>
                    ))

                  ) : (

                    <p>No missing skills detected.</p>

                  )}

                </div>

              </div>

              {/* RECOMMENDATIONS */}

              <div className="skills-result-card">

                <h3>
                  <Sparkles size={19} />
                  Improvement Suggestions
                </h3>

                <div className="suggestions-list">

                  {results.suggestions?.length > 0 ? (

                    results.suggestions.map((suggestion, index) => (
                      <div className="suggestion-item" key={index}>
                        <CheckCircle2 size={17} />
                        <p>{suggestion}</p>
                      </div>
                    ))

                  ) : (

                    <p>No suggestions available.</p>

                  )}

                </div>

              </div>

            </section>

          )}

          {/* FEATURES */}

          <section className="features-section">

            <div className="section-heading">

              <div>
                <h2>What you'll discover</h2>
                <p>
                  Everything you need to improve your career profile.
                </p>
              </div>

            </div>

            <div className="features-grid">

              <div className="feature-card">

                <div className="feature-icon purple">
                  <BarChart3 size={22} />
                </div>

                <h3>Resume Match Score</h3>

                <p>
                  Understand how closely your resume matches the target role.
                </p>

              </div>

              <div className="feature-card">

                <div className="feature-icon blue">
                  <Target size={22} />
                </div>

                <h3>Missing Skills</h3>

                <p>
                  Discover the important skills missing from your resume.
                </p>

              </div>

              <div className="feature-card">

                <div className="feature-icon green">
                  <Sparkles size={22} />
                </div>

                <h3>Improvement Suggestions</h3>

                <p>
                  Get useful recommendations to strengthen your resume.
                </p>

              </div>

            </div>

          </section>

          {/* FOOTER */}

          <footer className="footer">

            <p>© 2026 ResumeIQ. Built with intelligence.</p>

            <p>
              Made with <span>♥</span> for your next opportunity.
            </p>

          </footer>

        </div>

      </main>

    </div>
  )
}

export default App