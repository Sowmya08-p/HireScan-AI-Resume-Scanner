import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file"""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text.lower()

def clean_text(text):
    """Remove special characters and extra spaces"""
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def calculate_match(resume_text, jd_text):
    """Calculate similarity score using TF-IDF + Cosine Similarity"""
    documents = [resume_text, jd_text]
    tfidf = TfidfVectorizer(stop_words='english').fit_transform(documents)
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])
    return similarity[0][0] * 100

def get_missing_keywords(resume_text, jd_text):
    """Find important keywords from JD missing in resume"""
    resume_words = set(resume_text.split())
    jd_words = set(jd_text.split())
    # Get top 10 important words from JD
    important_words = [word for word in jd_words if len(word) > 4]
    missing = [word for word in important_words[:10] if word not in resume_words]
    return missing[:5]

if __name__ == "__main__":
    print("="*50)
    print(" 🔥 HireScan AI - Resume Scanner 🔥")
    print("="*50)

    resume_path = input("\n📄 Enter Resume PDF path: ")
    print("\n📝 Paste Job Description and press Enter twice:")
    jd_lines = []
    while True:
        line = input()
        if line:
            jd_lines.append(line)
        else:
            break
    jd_text = " ".join(jd_lines)

    print("\n⏳ Scanning your resume...")

    resume_text = extract_text_from_pdf(resume_path)
    resume_text = clean_text(resume_text)
    jd_text = clean_text(jd_text.lower())

    if not resume_text:
        print("❌ Could not read resume. Please check PDF file.")
        exit()

    match_score = calculate_match(resume_text, jd_text)
    missing_keywords = get_missing_keywords(resume_text, jd_text)

    print("\n" + "="*50)
    print(f" ✅ ATS Match Score: {match_score:.2f}%")
    print("="*50)

    if match_score >= 80:
        print("🟢 Excellent Match! Strong chance of getting shortlisted.")
    elif match_score >= 60:
        print("🟡 Good Match! Add more keywords to improve.")
    else:
        print("🔴 Low Match! Your resume needs major improvements.")

    print(f"\n💡 Top 5 Missing Keywords from JD: {', '.join(missing_keywords)}")
    print("\nTip: Add these keywords to your resume if you have those skills.")
  
