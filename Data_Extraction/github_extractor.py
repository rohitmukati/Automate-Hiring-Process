import requests
import re
import json

# ✅ GitHub se profile details extract karo
def extract_github_skills(profile_url):
    try:
        username = profile_url.rstrip('/').split('/')[-1]
        api_url = f"https://api.github.com/users/{username}/repos"
        response = requests.get(api_url)

        if response.status_code == 200:
            repos = response.json()

            # ✅ Repo ka data json ke form me ho na chiye
            if isinstance(repos, list):
                skills = set()
                for repo in repos:
                    if isinstance(repo, dict) and 'languages_url' in repo:
                        languages_url = repo['languages_url']
                        lang_response = requests.get(languages_url)
                        if lang_response.status_code == 200:
                            languages = lang_response.json().keys()
                            skills.update(languages)
                return list(skills)
            else:
                print(f"⚠️ No repo data for {profile_url}")
                return []
        else:
            print(f"❌ Error fetching profile data: {response.status_code}")
            return []
    except Exception as e:
        print(f"❌ Error in extracting GitHub data: {e}")
        return []


# ✅ Multiple links handle karne ka function
def extract_github_profiles(links):
    print(f"🔍 Extracting GitHub profiles from links")
    all_skills = {}
    
    for link in links:
        try:
            # ✅ Sirf profile link ko accept karega
            if re.match(r'https://github\.com/[^/]+/?$', link):
                username = link.rstrip('/').split('/')[-1]
                skills = extract_github_skills(link)
                if skills:
                    all_skills[username] = skills
            else:
                print(f"⚠️ Skipping non-profile link: {link}")
        except Exception as e:
            print(f"❌ Error in processing link {link}: {e}")

    return all_skills



# # ✅ Example Links (Profile + Repo Mix)
# github_links = [
#     "https://github.com/rohitmukati",  # Profile link
#     "https://github.com/rohitmukati/AI-Project",  # Repo link (skip hoga)
#      # Profile link
# ]

# # ✅ Data Fetching
# result = extract_github_profiles(github_links)
# print(result)
