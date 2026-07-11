# HireScan AI - Resume Scanner 🤖

An AI-powered ATS Resume Scanner that matches your resume with Job Descriptions and gives an ATS match score.

## 🚀 About The Project
Companies like TCS, Infosys use ATS to filter resumes. This project simulates that.
It extracts text from a PDF resume, compares it with a Job Description, and tells you the % match + missing keywords.

## 🛠️ Tech Stack
- **Language**: Python
- **Libraries**: PyPDF2
- **Concept**: NLP, Keyword Matching

## 📸 Demo Output
Here is the actual output of the scanner:

![ATS Score Demo](Demo.png)

**Output:**
*Note: The low score proves the AI is working. It detected that the resume was missing keywords from the JD.*

## ⚙️ How To Run
```bash
git clone https://github.com/Sowmya08-p/HireScan-AI-Resume-Scanner
cd HireScan-AI-Resume-Scanner
pip install -r requirements.txt
python app.py
