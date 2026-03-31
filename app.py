import streamlit as st
import utils

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):
    try:
        if uploaded_file is not None and job_desc.strip() != "":
            
            with st.spinner("Analyzing your resume..."):
                
                resume_text = utils.extract_text(uploaded_file)

                score, matching, missing = utils.analyze_resume(resume_text, job_desc)

                st.success("Analysis Complete ")

                st.write(f"## Match Score: {score}%")

                st.write("### Matching Skills:")
                if matching:
                    for skill in matching:
                        st.write(f"- {skill}")
                else:
                    st.write("No matching skills found")

                st.write("### Missing Skills:")
                if missing:
                    for skill in missing:
                        st.write(f"- {skill}")
                else:
                    st.write("No missing skills")

                st.write("### Suggestions:")
                if missing:
                    for skill in missing:
                        st.write(f"- Add experience with {skill}")
                else:
                    st.write("- Your resume matches the job well!")

        else:
            st.warning("Please upload resume and enter job description")

    except Exception as e:
        st.error(f"Error: {e}")
