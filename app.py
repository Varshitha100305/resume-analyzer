import streamlit as st
import utils

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)")
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if uploaded_file and job_desc:
        resume_text = utils.extract_text(uploaded_file)
        score, matching, missing = utils.analyze_resume(resume_text, job_desc)

        st.write(f"Match Score: {score}%")
        st.write("Matching Skills:", matching)
        st.write("Missing Skills:", missing)
