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
    text = text.lower()
    found_skills = []

