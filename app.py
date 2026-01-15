import streamlit as st
from src.extractor import extract_text
from src.preprocessing import clean_text
from src.skill_extraction import extract_skills
from src.recommender import skill_gap

# -------------------- UI CONFIG --------------------
st.set_page_config(
    page_title="Resume Skill Gap Analyzer",
    page_icon="📄",
    layout="centered"
)

st.title("📊 AI-Based Resume Skill Gap Analyzer")
st.write("Upload your resume and paste a job description to identify missing skills.")

# -------------------- INPUTS --------------------
resume_file = st.file_uploader(
    "📄 Upload Resume (PDF/DOCX)",
    type=["pdf", "docx"]
)

jd_text = st.text_area(
    "🧠 Paste Job Description",
    height=200
)

# -------------------- ANALYSIS --------------------
if st.button("🔍 Analyze"):
    if resume_file is None:
        st.warning("⚠️ Please upload a resume file.")
    elif not jd_text.strip():
        st.warning("⚠️ Please paste a job description.")
    else:
        # Extract & clean text
        resume_text = clean_text(extract_text(resume_file))
        jd_text_clean = clean_text(jd_text)

        # Extract skills
        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd_text_clean)

        # Skill gap
        missing_skills = skill_gap(jd_skills, resume_skills)

        # -------------------- RESULTS --------------------
        st.divider()

        st.subheader("✅ Extracted Resume Skills")
        if resume_skills:
            st.success(", ".join(resume_skills))
        else:
            st.info("No skills detected in resume.")

        st.subheader("❌ Missing Skills")
        if missing_skills:
            st.error(", ".join(missing_skills))
        else:
            st.success("Great match! No missing skills 🎉")

        # -------------------- MATCH SCORE --------------------
        if jd_skills:
            match_score = int(
                (len(resume_skills) / len(jd_skills)) * 100
            )
            st.metric("📈 Skill Match Percentage", f"{match_score}%")

        st.divider()
        st.caption("💡 Tip: Add missing skills to your resume or start learning them to improve your match.")
