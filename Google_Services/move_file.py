from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
import os
from dotenv import load_dotenv

load_dotenv()

# 🔹 Load folder IDs from environment variables
UNPROCESSED_FOLDER_ID = os.getenv("UNPROCESSED_FOLDER")
PROCESSED_FOLDER_ID = os.getenv("PROCESSED_FOLDER")
GOOGLE_SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_SERVICE_ACCOUNT_PATH")

creds = Credentials.from_service_account_file(GOOGLE_SERVICE_ACCOUNT_FILE, scopes=["https://www.googleapis.com/auth/drive"])
drive_service = build("drive", "v3", credentials=creds)


def move_file(file_id, moved_folder_id):
    """Move file from Unprocessed to Processed folder safely."""
    try:
        # 🔹 Get current parent folders of the file
        file = drive_service.files().get(fileId=file_id, fields="parents").execute()
        previous_parents = file.get("parents", [])

        # 🔹 Check if file is already in the processed folder
        if moved_folder_id in previous_parents:
            print(f"⚠️ File {file_id} is already in the processed folder.")
            return

        # 🔹 Move the file
        drive_service.files().update(
            fileId=file_id,
            addParents=moved_folder_id,
            removeParents=",".join(previous_parents),
            fields="id, parents"
        ).execute()

        print(f"✅ File {file_id} moved successfully!")

    except Exception as e:
        print(f"❌ Error moving file {file_id}: {str(e)}")

def move_files_by_dict(file_dict, moved_folder_id):
    """Move all files from the given dictionary."""
    print("Moving files...")
    print("====================================")
    for file_name, file_id in file_dict.items():
        print(f"🚀 Moving {file_name}...")
        move_file(file_id, moved_folder_id)
    print("All files moved successfully!")
    



            
# ids = {'Rohit_GenAi (1).pdf': '1-isftqOjcj0uHuBtTRDMoSiHWQCn8e04',
#        'Rohit_GenAi.pdf': '1lTmrLjCe32wDfzLmo_oRP4pmYfqA8u8M',
#        'long_video_demo.py': '1gSQyBa6IigbPbG1p-JFi7sSXHhqNYcfV',
#        'Rohit_GenAi (2).pdf': '1r5O7jKMOPfUho8sCyPBYyV1kWMh4K2Jx',
#        'Gourav_Panchal Resume.pdf': '1j6fJzbr_dn8-aAx6CLHFLztf45b0TRtV',
#        'Genai.pdf': '1vitw2FKY7CI0k2r7y8KnTXV-syWwBz4n'}

# move_files_by_dict(ids, PROCESSED_FOLDER_ID)
