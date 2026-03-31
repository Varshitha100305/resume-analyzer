import streamlit as st
import utils
from analyzer import analyze

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("AI Resume Analyzer")

st.write("Upload your resume and compare it with a job description")
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description")
if st.button("Analyze"):
    try:
        if uploaded_file is not None and job_desc.strip() != "":
            
            with st.spinner("Analyzing your resume..."):
                
                resume_text = utils.extract_text(uploaded_file)

                prompt = utils.create_prompt(resume_text, job_desc)

                result = analyze(prompt)

                st.success("Analysis Complete")
                st.write(result)

        else:
            st.warning("Please upload a resume and enter job description")

    except Exception as e:
        st.error(f"Error: {e}")
