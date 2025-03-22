# Automate Hiring Process

## 📌 Overview
This project automates the hiring process using AI agents. It extracts information from resumes, fetches GitHub and LinkedIn data, and matches candidates with job descriptions and assign score.

## 🚀 Features
- **Resume Parsing**: Extracts skills, experience, education, and links from resumes.
- **GitHub & LinkedIn Scraper**: Fetches profile data, skills, and repositories.
- **Candidate Matching**: Compares extracted data with job descriptions and assigns a score.
- **Google Sheets Integration**: Stores processed data for easy access.

## 🛠️ Tech Stack
- **Python** (FastAPI, CrewAI, PyMuPDF, Gemini API)
- **GitHub & LinkedIn API**
- **Google Sheets API**

## 📂 Project Structure
```
📦 Automate-Hiring-Process
├── Agent1
│   ├── agent1.py          # Resume parsing
│   ├── gemini_extractor.py # Extracts structured data
├── Agent2
│   ├── matching.py        # Candidate-job matching logic
│   ├── update_sheet.py    # Google Sheets integration
├── main.py                # Runs the pipeline
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

## ⚙️ Setup & Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/rohitmukati/Automate-Hiring-Process.git
cd Automate-Hiring-Process
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Configure API Keys
Create a `.env` file and add your keys:
```
GEMINI_API_KEY=your_key_here
GITHUB_ACCESS_TOKEN=your_token_here
LINKEDIN_API_KEY=your_key_here
GOOGLE_SHEET_JSON_PATH=your_json_file_path   ## add your json file client id for sheet, you can get your json file from google developer credentials page.
GOOGLE_SHEET_ID=your_sheet_id_here    ## you can find id from inside link of your google sheet
```
## FOR GOOGLE_SHEET_JSON_PATH & GOOGLE_SHEET_ID SETUP
1. Follow this [GOOGLE_SHEET_SETUP.md](https://github.com/rohitmukati/Automate-Hiring-Process/blob/main/GOOGLE_SHEET_SETUP.md) setup guide.

### 4️⃣ Run the Program
```bash
python main.py
```

## 🔥 Usage
1. Place resumes in the `input` folder.
2. The system will extract details and compare them with the job description.
3. Candidate ranking will be stored in Google Sheets.

## 🤝 Contributing
- Fork the repo
- Create a new branch (`git checkout -b feature-branch`)
- Commit your changes (`git commit -m 'Added new feature'`)
- Push and create a PR!

## 📜 License
This project is licensed under the Apache-2.0 license.

