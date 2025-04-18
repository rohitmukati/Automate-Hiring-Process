import os
from dotenv import load_dotenv
import google.generativeai as genai
import pdfplumber
import json
from pdf2docx import Converter
from docx import Document

# ✅ Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# ✅ Gemini ko initialize karo
genai.configure(api_key=GEMINI_API_KEY)






def extract_text_from_docx(file_path):
    """DOCX file se text extract karne ka function"""
    print("Extracting text from DOCX...")
    text = []
    try:
        doc = Document(file_path)
        for para in doc.paragraphs:
            text.append(para.text)  # Har paragraph ka text extract karna
    except Exception as e:
        print(f"❌ Error extracting text from DOCX: {e}")
        return None
    print("Extracted text from DOCX:" , text)
    
    return "\n".join(text)




## Extracting text
def extract_text_from_pdf(file_path):
    print("Extracting text from PDF...")
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() + '\n'  
    print("Extracted text from PDF:" , text)
    return text




def extracting_text_from_resume(pdf_path):
    print("checking file format")
    if pdf_path.endswith(".pdf"):
        text = extract_text_from_pdf(pdf_path)
        return text
    elif pdf_path.endswith(".docx"):
        text = extract_text_from_docx(pdf_path)
        return text
    else:
        print("❌ Invalid file format. Please provide a PDF or DOCX file.")
        return None




# ✅ LLM se skills, experience, education extract karo
def extract_with_gemini(text):
    print("Extracting information with Gemini...")
    prompt = f"""
    Extract the following information from this resume:
    1. Skills
    2. Experience
    3. Education
    4. Email
    5. Phone
    6. Prjoects
    Ensure that in project Just list down project name and the tech stack used in that project , Dont Describe hole project,
    Just only add relevent things dont try to add all the explanation 
    Ensure that in education it only contain name of school and collage with degree and year of passing.

    
    Resume:
    {text}
    And if you didn't get any information then place null
    if resume text is empty then just place null and return the output in JSON format like this:
    Return the output in JSON format like this:
    {{
      "Name": "Name",
      "Email": "email1",
      "Phone": "phone1",
      "City": "City",
      "Education": ["college name", "degree", "year of passing", ...],
      "Skills": ["skill1", "skill2", ...],
      "Experience": ["experience1 2021-2022", "experience2 may-jun","No Experience",...],
      "Projects": ["project1", "project2", ...]
    }}
    """
    
    # ✅ Use Gemini 2.0 Flash model
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    data = response.text
    return data
    
    

# ✅ Final Parsing Function
def parse_resume(pdf_path):
    text = extracting_text_from_resume(pdf_path)
    data = extract_with_gemini(text)
    return data


