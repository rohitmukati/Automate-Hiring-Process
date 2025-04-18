import gspread
from google.oauth2.service_account import Credentials
import json
from dotenv import load_dotenv
import os

# 🔹 Load environment variables
load_dotenv()
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_IDD")
GOOGLE_SERVICE_ACCOUNT_PATH = os.getenv("GOOGLE_SERVICE_ACCOUNT_PATH")


def update_sheet(json_data, score_data):
    print("Received JSON Data FOR Sheet Updating:", repr(json_data))
    json_data = json_data.strip()  # Extra spaces & newlines remove karo

    # ✅ Remove markdown formatting ```json ... ```
    if json_data.startswith("```json"):
        json_data = json_data[7:]  # First 7 characters (```json\n) remove karo
    if json_data.endswith("```"):
        json_data = json_data[:-3]

    if not json_data.strip():  # Agar json_data empty hai
        print("⚠️ Error: Empty JSON data received!")
        return

    try:
        data = json.loads(json_data)  # Convert JSON string to Python dict
    except json.JSONDecodeError as e:
        print("⚠️ JSON Decode Error:", e)
        return
    ## Removing markdown formating in score Data
    # ✅ Remove markdown formatting ```json ... ```
    if score_data.startswith("```json"):
        score_data = score_data[7:]  # First 7 characters (```json\n) remove karo
    if score_data.endswith("```"):
        score_data = score_data[:-3]

    if not score_data.strip():  # Agar json_data empty hai
        print("⚠️ Error: Empty JSON data received!")
        return

    try:
        score_data = json.loads(score_data)  # Convert JSON string to Python dict
    except json.JSONDecodeError as e:
        print("⚠️ JSON Decode Error:", e)
        return

    name = data["Name"]
    email = data["Email"]
    phone = data["Phone"]
    city = data["City"]
    
    score = score_data["score"]  # Score ko extract karo
    job_title = score_data["job_title"]  # Job title ko extract karo

    # ✅ Convert list to comma-separated string
    skills = ", ".join(data["Skills"]) if isinstance(data["Skills"], list) else data["Skills"]
    experience = ", ".join(data["Experience"]) if isinstance(data["Experience"], list) else data["Experience"]
    education = ", ".join(data["Education"]) if isinstance(data["Education"], list) else data["Education"]

    SERVICE_ACCOUNT_FILE = GOOGLE_SERVICE_ACCOUNT_PATH

    # 🔹 Scope define karo (Google Sheets access ke liye)
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

    # 🔹 Credentials load karo
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # 🔹 Google Sheets Access karo
    client = gspread.authorize(creds)

    # 🔹 Apne Google Sheet ka ID daalo (Sheet URL me se milega)
    SHEET_ID = GOOGLE_SHEET_ID

    # 🔹 Sheet open karo
    sheet = client.open_by_key(SHEET_ID).sheet1  # First sheet select

    # 🔹 Resume Data Insert Karo
    data = [name, email, phone, city, skills, experience, education, score,job_title ]  # Input data yaha dalna
    sheet.append_row(data)  # Data last row me add hoga

    print("** Data inserted successfully! **")
