from pypdf import PdfReader

def extract_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content
    return text


def extract_skills(text):
    skills = [
        "python", "sql", "machine learning", "deep learning",
        "nlp", "docker", "aws", "api", "pandas", "numpy",
        "tensorflow", "pytorch", "data analysis"
    ]

    text = text.lower()
    found_skills = []

    for skill in skills:
        if skill in text:
            found_skills.append(skill.title())

    return list(set(found_skills))

def analyze_resume(resume_text, job_desc):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_desc)

    matching = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))

    if len(job_skills) == 0:
        score = 0
    else:
        score = int((len(matching) / len(job_skills)) * 100)

    return score, matching, missing
