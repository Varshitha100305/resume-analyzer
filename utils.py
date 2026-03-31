from pypdf import PdfReader

def extract_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

def create_prompt(resume, job_desc):
    return f"""
Compare the resume and job description.

Give:
1. Match Score (%)
2. Missing Skills
3. Suggestions

Resume:
{resume}

Job Description:
{job_desc}
"""
