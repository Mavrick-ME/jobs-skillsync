import pdfplumber
from docx import Document
import os

def parse_resume(file_path: str) -> str:
    """
    Reads a resume file and returns extracted text.
    Supports PDF, DOCX, and TXT formats.
    """
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return parse_pdf(file_path)
    elif ext == ".docx":
        return parse_docx(file_path)
    elif ext == ".txt":
        return parse_txt(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")


def parse_pdf(file_path: str) -> str:
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    return text.strip()


def parse_docx(file_path: str) -> str:
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
    return text.strip()


def parse_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()


# Quick test — run this file directly to check it works
if __name__ == "__main__":
    test_path = input("Enter path to a resume file (PDF/DOCX/TXT): ")
    result = parse_resume(test_path)
    print("\n--- Extracted Text ---")
    print(result[:500])  # show first 500 characters
    print("...")
    print(f"\nTotal characters extracted: {len(result)}")