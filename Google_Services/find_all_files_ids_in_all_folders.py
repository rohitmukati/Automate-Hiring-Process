from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
import os
from dotenv import load_dotenv

load_dotenv()

# 🔹 Load credentials
GOOGLE_SHEET_JSON_PATH = os.getenv("GOOGLE_SHEET_JSON_PATH")
UNPROCESSED_FOLDER_ID = os.getenv("UNPROCESSED_FOLDER_ID")
PROCESSED_FOLDER_ID = os.getenv("PROCESSED_FOLDER_ID")
path = r"C:\Users\hp\Desktop\project\Automate-Hiring-Process\gen-lang-client-0812795063-300e2cb76181.json"

creds = Credentials.from_service_account_file(path, scopes=["https://www.googleapis.com/auth/drive"])
drive_service = build("drive", "v3", credentials=creds)

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
    unprocessed_folder_ids = get_all_file_ids(UNPROCESSED_FOLDER_ID)
    print("PROCESSED Files:")
    print(processed_folder_ids)
    print("UNPROCESSED Files:")
    print(unprocessed_folder_ids)
    return processed_folder_ids, unprocessed_folder_ids
