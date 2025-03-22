import requests
import re

# ✅ GitHub API token (optional for higher limit)
HEADERS = {'Authorization': 'token YOUR_GITHUB_ACCESS_TOKEN'}

# ✅ Function to extract tech stack from repo
def extract_repo_tech_stack(repo_url):
    repo_match = re.search(r'github\.com/([^/]+)/([^/]+)', repo_url)
    if not repo_match:
        print(f"⚠️ Invalid GitHub repo URL: {repo_url}")
        return None
    
    owner, repo = repo_match.groups()
    
    # ✅ Extract Languages
    languages_url = f'https://api.github.com/repos/{owner}/{repo}/languages'
    languages_response = requests.get(languages_url, headers=HEADERS).json()
    languages = list(languages_response.keys())
    
    # ✅ Extract Topics
    repo_url = f'https://api.github.com/repos/{owner}/{repo}'
    repo_response = requests.get(repo_url, headers=HEADERS).json()
    topics = repo_response.get('topics', [])
    
    return {
        'Languages': languages,
        'Frameworks': topics
    }

# ✅ Test with Multiple Repo Links
repo_links = [
    'https://github.com/rohitmukati/Text-Summarization-NLP',
    'https://github.com/rohitmukati/movies-recommended-system-2'
]

data = []
for link in repo_links:
    repo_data = extract_repo_tech_stack(link)
    if repo_data:
        data.append(repo_data)

print(data)
