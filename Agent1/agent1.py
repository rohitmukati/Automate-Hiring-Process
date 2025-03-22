from Agent1.gemini_extractor import parse_resume
from Agent1.links_extractor import classify_links
from Agent1.github_extractor import extract_github_profiles

def run_agent1(file_path):
    # ✅ Step 1: Resume data extract karo using Gemini
    resume_data = parse_resume(file_path)
    # print("\n🟢 Resume Data:\n", resume_data)

    # ✅ Step 2: Links extract karo and classify karo
    # github_links, linkedin_links, certificate_links = classify_links(file_path)
    # print("\n🟢 Extracted GitHub Links:\n", github_links)
    # print("\n🟢 Extracted LinkedIn Links:\n", linkedin_links)
    # print("\n🟢 Extracted Certificate Links:\n", certificate_links)

    # ✅ Step 3: GitHub se skills extract karo
    # if github_links:
    #     github_skills = extract_github_profiles(github_links)
        # print("\n🟢 GitHub Skills:\n", github_skills)

    # ✅ Step 4: Final Output ko merge karo
    # resume_data['GitHub Skills'] = github_skills if github_links else []

    return resume_data

# if __name__ == "__main__":
#     file_path = 'Genai.pdf'
#     data = run_agent1(file_path)
#     print("\n✅ Final Data:\n", data)
