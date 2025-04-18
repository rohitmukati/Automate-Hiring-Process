from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
import os
from dotenv import load_dotenv
load_dotenv()

# 🔹 Load credentials
# 🔹 Service Account JSON File ka Path
GOOGLE_SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")
if os.path.exists(GOOGLE_SERVICE_ACCOUNT_FILE):
    print("✅ Service account file found!")
else:
    print("❌ Error: Service account file not found! Check the file path.")
 # Agar False return kare to path galat hai


UNPROCESSED_FOLDER_ID = os.getenv("UNPROCESSED_FOLDER")
PROCESSED_FOLDER_ID = os.getenv("PROCESSED_FOLDER")
print(f"Loaded UNPROCESSED_FOLDER_ID: {UNPROCESSED_FOLDER_ID}")
print(f"Loaded UNPROCESSED_FOLDER_ID: {PROCESSED_FOLDER_ID}")

# path = r"C:\Users\hp\Desktop\project\Automate-Hiring-Process\gen-lang-client-0812795063-300e2cb76181.json"

try:
    # 🔹 Credentials Load Karo
    creds = Credentials.from_service_account_file(GOOGLE_SERVICE_ACCOUNT_FILE, scopes=["https://www.googleapis.com/auth/drive"])
    # 🔹 Drive Service Initialize Karo
    drive_service = build("drive", "v3", credentials=creds)
    print("✅ Success: Connected to Google Drive!")
except Exception as e:
    print(f"❌ Error while connecting to drive: {e}")


def get_all_file_ids(folder_id):
    """Folder ke andar jitni bhi files hai, unki IDs return karega."""
    print(f"Fetching files from folder ID: {folder_id}")
    query = f"'{folder_id}' in parents and trashed=false"
    results = drive_service.files().list(q=query, fields="files(id, name)").execute()
    files = results.get("files", [])

    file_ids = {file["name"]: file["id"] for file in files}
    return file_ids


def both_folder_files_id():
    processed_folder_ids = get_all_file_ids(PROCESSED_FOLDER_ID)
    unprocessed_folder_ids = get_all_file_ids(UNPROCESSED_FOLDER_ID)  # ✅ Corrected

    print("PROCESSED Files:")
    print(processed_folder_ids)
    print("UNPROCESSED Files:")
    print(unprocessed_folder_ids)

    return processed_folder_ids, unprocessed_folder_ids


both_folder_files_id()