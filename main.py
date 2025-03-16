from fastapi import FastAPI
from services import get_user_repos, get_repo_commits, get_repo_details

app = FastAPI(title="MCP Server for GitHub AI Integration")

@app.get("/")
def read_root():
    return {"message": "Welcome to the MCP Server for GitHub"}

@app.get("/repos/{username}")
def fetch_repos(username: str):
    """Fetch GitHub repositories of a user"""
    return get_user_repos(username)

@app.get("/commits/{username}/{repo}")
def fetch_commits(username: str, repo: str):
    """Fetch recent commits of a repository"""
    return get_repo_commits(username, repo)

@app.get("/repo_details/{username}/{repo}")
def fetch_repo_details(username: str, repo: str):
    """Fetch details of a repository"""
    return get_repo_details(username, repo)