# 🔍 GitHub Profile Analyzer — AI-Powered Developer Insights

A modern, full-stack web application that analyzes any GitHub profile and generates intelligent insights using **Google Gemini AI**. Built with **FastAPI** and Vanilla JS.

🌐 **Live Demo:** https://github-ai-analyzer-rust.vercel.app/

---

## 🚀 What It Does

Enter any GitHub username → it fetches their public profile, repos, and language stats → sends it to Gemini AI → generates a structured developer report with:

- 📊 Profile overview (repos, followers, stars, top languages)
- 🤖 AI-generated developer summary
- ✅ Strengths & areas to improve
- ⭐ Recruiter score out of 10
- 💡 Actionable recommendation

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|------|---------|---------|
| **Backend** | Python & FastAPI | High-performance REST API |
| **Frontend** | HTML, CSS, JavaScript | Premium dark mode UI with glassmorphism |
| **Data Source** | GitHub REST API | Fetch public profile data |
| **AI Engine** | Google Gemini AI | Generate intelligent developer insights |
| **Deployment**| Vercel | Serverless hosting |

---

## ⚙️ Setup & Installation (Local Development)

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

### 5. Run the Local Server
Start the FastAPI application using uvicorn:
```bash
uvicorn api.index:app --reload
```
Then, open your browser and go to `http://127.0.0.1:8000` to use the application!
