import streamlit as st
from utils import extract_text, create_prompt
from analyzer import analyze

st.title("AI Resume Analyzer")

st.write("App started")

uploaded_file = st.file_uploader("Upload Resume (PDF)")
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):
    try:
        if uploaded_file and job_desc:
            st.write("Processing...")

            resume_text = extract_text(uploaded_file)
            st.write("Resume extracted")

            prompt = create_prompt(resume_text, job_desc)

            result = analyze(prompt)
            st.write("Analysis done")

            st.write(result)

        else:
            st.warning("Please upload resume and enter job description")

    except Exception as e:
        st.error(f"Error: {e}")
