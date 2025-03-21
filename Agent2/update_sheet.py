import gspread
from google.oauth2.service_account import Credentials
import json
from dotenv import load_dotenv
import os

# 🔹 Service Account JSON file ka path (Tumhare downloaded JSON file ka actual path yahan daalo)

load_dotenv()
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
GOOGLE_SHEET_JSON_PATH = os.getenv("GOOGLE_SHEET_JSON_PATH")


def update_sheet(json_data, score):
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
    
    
    name = data["Name"]
    email = data["Email"]
    phone = data["Phone"]
    city = data["City"]

    
    SERVICE_ACCOUNT_FILE = GOOGLE_SHEET_JSON_PATH

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

# 🔹 Resume Data Insert Karo (Example Data)
# Data insert karna
    data = [name, email, phone, city, score]  # Input data yaha dalna
    sheet.append_row(data)  # Data last row me add hoga

    print("** Data inserted successfully! **")