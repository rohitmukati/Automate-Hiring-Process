import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------------------------------------------
# 1) PAGE CONFIG
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="HR Summary Dashboard",
    layout="wide",  # Use the entire screen width
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------
# 2) SAMPLE DATA
# ----------------------------------------------------------------------
# A) Processed Mails
mails_data = {
    "Time": ["10:00 AM", "10:15 AM", "10:30 AM", "11:00 AM"],
    "Subject": ["Resume for AI/ML", "Resume for Developer", "Internship Inquiry", "Resume for Data Analyst"],
    "Status": ["Processed", "Unprocessed", "Processed", "Processed"]
}
df_mails = pd.DataFrame(mails_data)

# B) Processed Resumes
resumes_data = {
    "FileName": ["Rohit_Resume.pdf", "Rahul_Resume.pdf", "Neha_Resume.pdf"],
    "ProcessedTime": ["10:10 AM", "10:20 AM", "10:35 AM"],
    "Status": ["Processed", "Processed", "Processed"]
}
df_resumes = pd.DataFrame(resumes_data)

# C) Candidates
candidates_data = {
    "Name": ["Rohit", "Rahul", "Neha", "Priya", "Karan"],
    "Role Applied": ["AI/ML", "Developer", "Data Analyst", "AI/ML", "DevOps"],
    "Experience": [0, 2, 1, 3, 5],
    "Score": [55, 70, 60, 80, 90],
    "Status": ["In-Process", "Shortlisted", "In-Process", "Shortlisted", "Rejected"]
}
df_candidates = pd.DataFrame(candidates_data)

# ----------------------------------------------------------------------
# 3) SIDEBAR NAVIGATION
# ----------------------------------------------------------------------
st.sidebar.title("HR Dashboard Menu")
menu_options = [
    "Summary",
    "Process Mails",
    "Process Resumes",
    "Candidates",
    "Schedule Meet",
    "Visualize Candidates"
]
choice = st.sidebar.radio("Go to", menu_options)

# ----------------------------------------------------------------------
# 4) PAGE: SUMMARY
# ----------------------------------------------------------------------
if choice == "Summary":
    st.title("HR Summary Dashboard")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Processed Mails", value=len(df_mails[df_mails['Status'] == 'Processed']))
    with col2:
        st.metric(label="Total Processed Resumes", value=len(df_resumes))
    with col3:
        st.metric(label="Total Candidates", value=len(df_candidates))

    # Simple bar chart of candidates by role
    st.subheader("Headcount by Role Applied")
    role_count = df_candidates['Role Applied'].value_counts().reset_index()
    role_count.columns = ['Role', 'Count']
    fig_role = px.bar(role_count, x='Role', y='Count', title="Candidates by Role")
    st.plotly_chart(fig_role, use_container_width=True)

# ----------------------------------------------------------------------
# 5) PAGE: PROCESS MAILS
# ----------------------------------------------------------------------
elif choice == "Process Mails":
    st.title("Process Mails")
    st.write("Below is the list of mails fetched/processed within a time range.")
    
    # Show mails table
    st.dataframe(df_mails)

    # Filter by status
    status_filter = st.selectbox("Filter by Status", ["All", "Processed", "Unprocessed"])
    if status_filter != "All":
        filtered_mails = df_mails[df_mails['Status'] == status_filter]
    else:
        filtered_mails = df_mails
    st.write("Filtered Mails:")
    st.dataframe(filtered_mails)

# ----------------------------------------------------------------------
# 6) PAGE: PROCESS RESUMES
# ----------------------------------------------------------------------
elif choice == "Process Resumes":
    st.title("Process Resumes")
    st.write("List of resumes that have been processed and moved to the processed folder.")

    st.dataframe(df_resumes)

# ----------------------------------------------------------------------
# 7) PAGE: CANDIDATES
# ----------------------------------------------------------------------
elif choice == "Candidates":
    st.title("Candidates")
    st.write("All candidates extracted from resumes and their details.")
    
    # Filter by role
    roles = df_candidates["Role Applied"].unique().tolist()
    role_filter = st.selectbox("Filter by Role", ["All"] + roles)
    if role_filter != "All":
        filtered_candidates = df_candidates[df_candidates["Role Applied"] == role_filter]
    else:
        filtered_candidates = df_candidates

    st.dataframe(filtered_candidates)

    st.write("---")
    st.subheader("Candidate Detail View")
    candidate_list = filtered_candidates["Name"].unique().tolist()
    selected_candidate = st.selectbox("Select Candidate", candidate_list)
    
    candidate_info = filtered_candidates[filtered_candidates["Name"] == selected_candidate].iloc[0]
    st.write(f"**Name:** {candidate_info['Name']}")
    st.write(f"**Role Applied:** {candidate_info['Role Applied']}")
    st.write(f"**Experience:** {candidate_info['Experience']} years")
    st.write(f"**Score:** {candidate_info['Score']}")
    st.write(f"**Status:** {candidate_info['Status']}")

# ----------------------------------------------------------------------
# 8) PAGE: SCHEDULE MEET
# ----------------------------------------------------------------------
elif choice == "Schedule Meet":
    st.title("Schedule Meeting")
    st.write("Here you can schedule interviews/meetings with candidates.")
    
    # Simple scheduling form
    with st.form("schedule_form"):
        candidate_name = st.selectbox("Candidate", df_candidates["Name"].unique())
        date = st.date_input("Date")
        time = st.time_input("Time")
        meeting_mode = st.selectbox("Meeting Mode", ["Google Meet", "Zoom", "MS Teams"])
        submit_btn = st.form_submit_button("Schedule")

    if submit_btn:
        st.success(f"Meeting scheduled with **{candidate_name}** on **{date} {time}** via **{meeting_mode}**!")

# ----------------------------------------------------------------------
# 9) PAGE: VISUALIZE CANDIDATES
# ----------------------------------------------------------------------
elif choice == "Visualize Candidates":
    st.title("Visualize Candidates")
    
    # 1) Bar chart of Scores
    st.subheader("Bar Chart of Candidate Scores")
    fig_scores = px.bar(
        df_candidates, 
        x="Name", 
        y="Score", 
        color="Role Applied",
        title="Candidate Scores by Name"
    )
    st.plotly_chart(fig_scores, use_container_width=True)

    # 2) Another chart: Experience distribution
    st.subheader("Experience Distribution")
    fig_exp = px.histogram(
        df_candidates, 
        x="Experience", 
        nbins=5, 
        title="Distribution of Candidate Experience"
    )
    st.plotly_chart(fig_exp, use_container_width=True)

# ----------------------------------------------------------------------
# END
# ----------------------------------------------------------------------
