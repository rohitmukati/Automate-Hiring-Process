import streamlit as st
import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
GOOGLE_DRIVE_FOLDER_ID = os.getenv("GOOGLE_DRIVE_FOLDER_ID")
GOOGLE_SHEET_JSON_PATH = os.getenv("GOOGLE_SHEET_JSON_PATH")

# Google Drive API Setup
SERVICE_ACCOUNT_FILE = GOOGLE_SHEET_JSON_PATH  # Path to your service account JSON file
FOLDER_ID = GOOGLE_DRIVE_FOLDER_ID

# Authenticate with Google Drive API
creds = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=["https://www.googleapis.com/auth/drive"]
)
drive_service = build("drive", "v3", credentials=creds)

# Streamlit Dashboard UI
st.title("📄 Resume Upload Portal")
st.write("Upload your resume (PDF Only) to our Google Drive folder.")

# Resume Upload Section
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file:
    try:
        # Save the uploaded file to a temporary location
        file_path = f"temp_{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Prepare file metadata and upload the file to the specified Google Drive folder
        file_metadata = {"name": uploaded_file.name, "parents": [FOLDER_ID]}
        media = MediaFileUpload(file_path, mimetype="application/pdf")
        drive_service.files().create(
            body=file_metadata, media_body=media, fields="id"
        ).execute()
        
        st.success("✅ Resume uploaded successfully to Google Drive!")
    except Exception as e:
        st.error(f"❌ Error uploading resume: {e}")
    
