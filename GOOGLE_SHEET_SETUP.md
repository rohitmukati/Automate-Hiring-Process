# Google Sheets API Setup Guide

This guide will help you set up Google Sheets API integration with your project. Follow the steps carefully to ensure a successful configuration.
You can find your Json File & Your Sheet ID from this Steps
---

## **Step 1: Download Google Sheets API JSON File**
1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create or select a project.
3. Navigate to **APIs & Services > Credentials**.
4. Click **Create Credentials** > **Service Account**.
5. Fill in the required details and create the service account.
6. Go to the **Keys** section and click **Add Key > JSON**.
7. Download the JSON file and store it in your project directory (e.g., `credentials.json`).

---

## **Step 2: Share Access with Google Sheets API**
1. Open the downloaded `credentials.json` file.
2. Find the `client_email` field inside the JSON file.
3. Open your **Google Sheet**.
4. Click **Share** (top-right corner of the sheet).
5. Paste the `client_email` from `credentials.json` into the **Add people and groups** field.
6. Set the permission to **Editor** and click **Send**.

---

## **Step 3: Add JSON File Path to .env**
1. Open your project’s `.env` file.
2. Add the following line:
   ```env
   GOOGLE_SHEET_CREDENTIALS=path/to/credentials.json
   ```
   **Example:** If `credentials.json` is in the main folder, use:
   ```env
   GOOGLE_SHEET_CREDENTIALS=./credentials.json
   ```

---

## **Step 4: Add Google Sheet ID to .env**
1. Open your Google Sheet.
2. Copy the Sheet ID from the URL:
   ```
   https://docs.google.com/spreadsheets/d/<<SHEET_ID>>/edit
   ```
3. Open `.env` and add:
   ```env
   GOOGLE_SHEET_ID=your_google_sheet_id
   ```

---

## **Step 5: Verify `.gitignore`**
To ensure the JSON file is not pushed to Git, add this line to your `.gitignore` file:
```gitignore
credentials.json
```
Run the following command to confirm it's ignored:
```bash
git status
```
If `credentials.json` is in the untracked files list, remove it from Git cache:
```bash
git rm --cached credentials.json
```
Then commit and push again.

✅ **Your Google Sheets API is now set up and ready to use!** 🚀

