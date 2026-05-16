# 🔍 GitHub Profile Analyzer — AI-Powered Developer Insights

A command-line tool that analyzes any GitHub profile and generates intelligent insights using **Google Gemini AI**. Built with Python.

---

## 🚀 What It Does

Give it any GitHub username → it fetches their public profile, repos, and language stats → sends it to Gemini AI → generates a structured developer report with:

- 📊 Profile overview (repos, followers, stars, top languages)
- 🤖 AI-generated developer summary
- ✅ Strengths & areas to improve
- ⭐ Recruiter score out of 10
- 💡 Actionable recommendation

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| GitHub REST API | Fetch public profile data |
| Google Gemini AI | Generate intelligent insights |
| python-dotenv | Secure API key management |

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/nidhishkumarr18-arch/github-ai-analyzer.git
cd github-ai-analyzer
```

### 2. Set Up Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
Create a `.env` file in the project root:
```bash
touch .env
```
Add your Gemini API Key and GitHub Personal Access Token to the `.env` file:
```text
GEMINI_API_KEY=your_gemini_key_here
GITHUB_TOKEN=your_github_token_here
```

### 5. Run the Project
Run the analyzer on any GitHub username:
```bash
python3 main.py --user torvalds
```
