from pypdf import PdfReader

def extract_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content
    return text

def analyze_resume(resume_text, job_desc):
    resume_text = resume_text.lower()
    job_desc = job_desc.lower()

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
    resume_skills = [s for s in skills if s in resume_text]
    job_skills = [s for s in skills if s in job_desc]

    matching = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))

    score = int((len(matching) / len(job_skills)) * 100) if job_skills else 0

    return score, matching, missing
