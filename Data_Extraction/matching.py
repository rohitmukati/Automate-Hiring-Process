import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

# ✅ Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ✅ Gemini ko configure karo
genai.configure(api_key=GEMINI_API_KEY)

def get_score(resume_data, job_description):
    # ✅ Prompt ke liye JSON ko readable format me convert karo
    print("Getting Score of of resume data with job description")
    resume_data_str = json.dumps(resume_data, indent=2)
    
    prompt = f"""
Match the following resume data with the given job description and provide a similarity score.
Compare **only** the skills and experience with the job description and return a final score out of 100.

### Resume Data:
{resume_data_str}

### Job Description:
{job_description}

### Scoring Criteria:
1. Matching Skills
2. Matching Experience
3. Missing Skills
4. Overall Fit Percentage
More Foucus on their Skills and Experience for the score.

### Output Format (Strictly return only this format, no extra text):
99
After evaluating the candidate's resume and analyzing the job description,
determine the most suitable job role that aligns with their skills, experience, and qualifications.
Provide a concise yet specific job title (e.g., Java Developer, Data Analyst, Machine Learning Engineer, intern, Ai intern) that best fits the candidate's profile and industry standards.
give me final output for bothe score and job title in this format:
in json format:

{{
    "score": 99,
    "job_title": "Best Suitable profile"
}}
"""

    

    # ✅ Use Gemini 2.0 Flash model
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    data = response.text
    return data
    


