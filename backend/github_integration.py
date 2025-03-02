import requests
import os
from dotenv import load_dotenv

# .env fájl betöltése
load_dotenv()

# Biztonságos GitHub Token kezelés
GITHUB_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

def post_github_comment(repo: str, pr_number: int, comment: str):
    """PR-hez automatikusan AI alapú kommenteket küld."""
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    payload = {"body": comment}
    response = requests.post(url, json=payload, headers=HEADERS)
    return response.json()
