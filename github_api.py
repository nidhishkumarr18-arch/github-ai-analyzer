import requests
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_user_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Error: Could not fetch user '{username}'")
        return None
    return response.json()

def get_user_repos(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=100&sort=updated"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Error: Could not fetch repos for '{username}'")
        return []
    return response.json()

def get_language_stats(repos):
    language_count = {}
    for repo in repos:
        lang = repo.get("language")
        if lang:
            language_count[lang] = language_count.get(lang, 0) + 1
    return dict(sorted(language_count.items(), key=lambda x: x[1], reverse=True))

def get_summary_data(username):
    profile = get_user_profile(username)
    if not profile:
        return None

    repos = get_user_repos(username)
    languages = get_language_stats(repos)

    starred_repos = [r for r in repos if r["stargazers_count"] > 0]
    total_stars = sum(r["stargazers_count"] for r in repos)

    return {
        "username": username,
        "name": profile.get("name", "N/A"),
        "bio": profile.get("bio", "N/A"),
        "public_repos": profile.get("public_repos", 0),
        "followers": profile.get("followers", 0),
        "following": profile.get("following", 0),
        "total_stars": total_stars,
        "top_languages": languages,
        "repos": [
            {
                "name": r["name"],
                "description": r.get("description", "No description"),
                "stars": r["stargazers_count"],
                "language": r.get("language", "Unknown"),
                "url": r["html_url"]
            }
            for r in repos[:10]  # top 10 most recently updated
        ]
    }
