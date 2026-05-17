from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

try:
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
except Exception as e:
    client = None
    print(f"Warning: Failed to initialize Gemini client: {e}")

def analyze_profile(data):
    top_langs = ", ".join(list(data["top_languages"].keys())[:5]) or "None detected"
    repo_summaries = "\n".join([
        f"- {r['name']} ({r['language']}): {r['description']} | Stars: {r['stars']}"
        for r in data["repos"]
    ])

    prompt = f"""
You are a senior software engineer reviewing a GitHub profile for a software engineering internship.

Here is the GitHub profile data:

Name: {data['name']}
Bio: {data['bio']}
Public Repos: {data['public_repos']}
Followers: {data['followers']}
Total Stars: {data['total_stars']}
Top Languages: {top_langs}

Recent Repositories:
{repo_summaries}

Based on this data, provide:
1. Developer Summary - Who is this developer? What do they focus on? (2-3 sentences)
2. Strengths - What stands out positively? (3 bullet points)
3. Areas to Improve - What is missing or weak? (3 bullet points)
4. Recruiter Score - Rate this profile out of 10 for an engineering internship, with a one-line reason.
5. Top Recommendation - One specific action they can take to improve their GitHub profile.

Be honest, specific, and actionable. Avoid generic advice.
"""

    if not client:
        return "AI Insights are unavailable. Please ensure GEMINI_API_KEY is configured in Vercel."
        
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"AI Analysis failed: {str(e)}"
