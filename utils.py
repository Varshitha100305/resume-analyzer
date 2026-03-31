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
    # Programming
    "python", "java", "c++", "c", "javascript", "typescript",

    # Data & Analysis
    "sql", "mysql", "postgresql", "mongodb", "data analysis",
    "data science", "data visualization", "excel", "power bi", "tableau",

    # ML / AI Core
    "machine learning", "ml", "deep learning", "ai", "artificial intelligence",
    "supervised learning", "unsupervised learning", "reinforcement learning",

    # NLP / LLM
    "nlp", "natural language processing", "transformers",
    "hugging face", "langchain", "llm", "rag", "chatbot",

    # Frameworks / Libraries
    "pandas", "numpy", "scikit-learn", "sklearn",
    "tensorflow", "keras", "pytorch", "opencv",

    # Web / Backend
    "flask", "django", "fastapi", "rest api", "api", "apis",

    # Cloud / DevOps
    "aws", "amazon web services", "gcp", "google cloud",
    "azure", "docker", "kubernetes", "ci/cd", "jenkins",

    # Software Engineering
    "data structures", "algorithms", "oops", "object oriented programming",
    "system design", "design patterns", "problem solving",

    # Tools
    "git", "github", "gitlab", "linux", "bash",

    # Big Data
    "hadoop", "spark", "pyspark",

    # MLOps
    "mlops", "model deployment", "model serving", "airflow"
]
    skill_map = {
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "nlp": "natural language processing",
    "apis": "api",
    "restful api": "api",
    "aws cloud": "aws",
    "gcp cloud": "gcp"
}
def normalize_skill(skill):
    return skill_map.get(skill.lower(), skill.lower())

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
