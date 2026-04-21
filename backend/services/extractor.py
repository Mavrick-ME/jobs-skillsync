import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Master skills list
SKILLS_DB = [
    # Programming Languages
    "python", "java", "javascript", "typescript", "c++", "c#", "r", "go",
    "rust", "kotlin", "swift", "php", "ruby", "scala", "matlab",

    # Web Frameworks
    "django", "fastapi", "flask", "react", "next.js", "vue.js", "angular",
    "node.js", "express", "spring", "laravel",

    # ML & AI
    "machine learning", "deep learning", "nlp", "natural language processing",
    "computer vision", "tensorflow", "pytorch", "keras", "scikit-learn",
    "bert", "transformers", "huggingface", "opencv", "xgboost", "lightgbm",

    # Data
    "pandas", "numpy", "matplotlib", "seaborn", "tableau", "power bi",
    "sql", "mysql", "postgresql", "mongodb", "redis", "elasticsearch",
    "apache spark", "hadoop", "etl", "data wrangling", "data cleaning",

    # DevOps & Cloud
    "docker", "kubernetes", "jenkins", "git", "github", "gitlab",
    "aws", "azure", "gcp", "terraform", "ansible", "linux", "bash",
    "ci/cd", "nginx", "prometheus", "grafana",

    # Other
    "rest api", "graphql", "microservices", "agile", "scrum",
    "unit testing", "pytest", "jest", "figma"
]

def extract_skills(text: str) -> list:
    """Extract skills from resume text."""
    text_lower = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text_lower:
            found_skills.append(skill)

    return list(set(found_skills))


def extract_info(text: str) -> dict:
    """Extract structured info from resume using spaCy NER."""
    doc = nlp(text)

    # Extract named entities
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    orgs = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    dates = [ent.text for ent in doc.ents if ent.label_ == "DATE"]

    # Extract skills
    skills = extract_skills(text)

    return {
        "name": names[0] if names else "Unknown",
        "organizations": orgs[:5],
        "dates": dates[:5],
        "skills": skills,
        "skill_count": len(skills)
    }