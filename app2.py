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
SERVICE_ACCOUNT_FILE = GOOGLE_SHEET_JSON_PATH
FOLDER_ID = GOOGLE_DRIVE_FOLDER_ID

# Authenticate with Google Drive API
creds = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=["https://www.googleapis.com/auth/drive"]
)
drive_service = build("drive", "v3", credentials=creds)

# ... (Previous imports and Google Drive code remain same)

# Custom CSS with Vibrant Gradients
st.markdown("""
    <style>
        /* Rainbow Gradient Title */
        .rainbow-text {
            background: linear-gradient(90deg, #FF6B6B, #FFE66D, #4ECDC4, #45B7D1, #96CEB4, #FFEEAD);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            font-weight: 800;
            animation: rainbow_animation 6s ease-in-out infinite;
            background-size: 400% 100%;
        }
        
        @keyframes rainbow_animation {
            0%,100% { background-position: 0 0; }
            50% { background-position: 100% 0; }
        }

        /* Glassmorphism Upload Section */
        .upload-container {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 2rem;
            margin: 2rem 0;
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255,255,255,0.3);
            box-shadow: 0 8px 32px rgba(31, 38, 135, 0.15);
            background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(245,245,245,0.9));
        }

        /* Gradient Button Styling */
        .stButton>button {
            background: linear-gradient(135deg, #FF6B6B 0%, #FFE66D 100%);
            color: white !important;
            border: none;
            border-radius: 12px;
            padding: 12px 30px;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 15px rgba(255,107,107,0.4);
        }

        /* Modern Progress Bar */
        .stProgress > div > div {
            background: linear-gradient(90deg, #4ECDC4 0%, #45B7D1 100%);
            border-radius: 8px;
        }

    </style>
""", unsafe_allow_html=True)

# Main Header with Animation
st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <h1 class="rainbow-text">🌈 Resume Upload Wizard</h1>
        <h3 style="color: #555; font-weight: 400;">
            Your Gateway to Amazing Opportunities
        </h3>
    </div>
""", unsafe_allow_html=True)

# Upload Section with Glass Effect
with st.container():
    st.markdown('<div class="upload-container">', unsafe_allow_html=True)
    
    st.markdown("""
        <div style="text-align: center;">
            <h2 style="color: #4ECDC4; margin-bottom: 1rem;">✨ Drag & Drop Magic</h2>
            <p style="color: #666; line-height: 1.6;">
                Upload your resume and let our AI-powered system<br>
                find your perfect career match!
            </p>
        </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(" ", type=["pdf"], key="resume_uploader")
    
    st.markdown("""
        <div style="text-align: center; margin-top: 1.5rem;">
            <p style="color: #999; font-size: 0.9rem;">
                Supported formats: PDF (Max 5MB)<br>
                <span style="font-size: 1.5rem;">📎</span>
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ... (Rest of the Google Drive code remains same)

# File processing logic (unchanged)
if uploaded_file:
    try:
        # Save the uploaded file to a temporary location
        file_path = f"temp_{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Prepare file metadata and upload the file
        file_metadata = {"name": uploaded_file.name, "parents": [FOLDER_ID]}
        media = MediaFileUpload(file_path, mimetype="application/pdf")
        drive_service.files().create(
            body=file_metadata, media_body=media, fields="id"
        ).execute()
        
        st.markdown('<p class="success-message">✅ Resume uploaded successfully to Google Drive!</p>', unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f'<p class="error-message">❌ Error uploading resume: {e}</p>', unsafe_allow_html=True)

# Additional Info Section
st.markdown("""
    <div style="text-align: center; margin-top: 3rem; color: #777;">
        <h4>🔒 Secure & Confidential</h4>
        <p>Your resume is stored securely in our Google Drive and will only be accessed by authorized personnel</p>
    </div>
""", unsafe_allow_html=True)