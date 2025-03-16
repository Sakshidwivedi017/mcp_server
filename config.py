import os
from dotenv import load_dotenv

# ✅ Load environment variables from .env file
load_dotenv()

# ✅ GitHub API URL
GITHUB_API_URL = "https://api.github.com"

# ✅ Get GitHub Access Token from .env
GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")

# ✅ Validate the token before using it
if not GITHUB_ACCESS_TOKEN:
    raise ValueError("⚠️ GITHUB_ACCESS_TOKEN is missing. Please check your .env file!")

# ✅ Headers for GitHub API requests
HEADERS = {
    "Authorization": f"Bearer {GITHUB_ACCESS_TOKEN}",
    "Accept": "application/vnd.github.v3+json"  # Ensures latest GitHub API version
}