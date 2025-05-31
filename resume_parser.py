# resume_parser.py
import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_skills_experience(text):
    import re
    # Very simple keyword match - improve later
    skills_keywords = ["Python", "Java", "SQL", "React", "Node.js", "Django", "Spring Boot"]
    experience_years = re.findall(r"(\d+)\s+years", text)

    skills_found = [skill for skill in skills_keywords if skill.lower() in text.lower()]
    experience = experience_years[0] if experience_years else "N/A"

    return {
        "skills": skills_found,
        "experience": experience
    }

# Usage:
if __name__ == "__main__":
    text = extract_text_from_pdf("sample_resume.pdf")
    parsed = extract_skills_experience(text)
    print(parsed)
