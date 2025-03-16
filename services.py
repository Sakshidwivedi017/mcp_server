import requests
from config import GITHUB_API_URL, HEADERS

def get_user_repos(username: str):
    """Fetch user repositories from GitHub."""
    url = f"{GITHUB_API_URL}/users/{username}/repos"
    response = requests.get(url, headers=HEADERS) 
    if response.status_code == 200:
        return response.json()
    return {"error": response.json()}

def get_repo_commits(username: str, repo: str):
    """Fetch recent commits of a repository."""
    url = f"{GITHUB_API_URL}/repos/{username}/{repo}/commits"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    return {"error": response.json()}

def get_repo_details(username: str, repo: str):
    """Fetch details of a repository."""
    url = f"{GITHUB_API_URL}/repos/{username}/{repo}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    return {"error": response.json()}