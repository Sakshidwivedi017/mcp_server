import os
from dotenv import load_dotenv


load_dotenv()


GITHUB_API_URL = "https://api.github.com"


GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")


if not GITHUB_ACCESS_TOKEN:
    raise ValueError("GITHUB_ACCESS_TOKEN is missing. Please check your .env file!")


HEADERS = {
    "Authorization": f"Bearer {GITHUB_ACCESS_TOKEN}",
    "Accept": "application/vnd.github.v3+json"  # Ensures latest GitHub API version
}
