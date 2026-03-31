from pypdf import PdfReader

def extract_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content
    return text


def create_prompt(resume, job_desc):
    return f"""
Compare the resume and job description.

Give:
1. Matching skills
2. Missing skills
3. Suggestions

Resume:
{resume}

Job Description:
{job_desc}
"""
