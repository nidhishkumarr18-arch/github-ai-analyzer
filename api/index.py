from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import sys
import os

# Add parent directory to path so we can import our existing modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from github_api import get_summary_data
from ai_analyzer import analyze_profile

app = FastAPI(title="GitHub AI Analyzer API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/analyze")
def analyze(user: str):
    if not user:
        raise HTTPException(status_code=400, detail="Username is required")
        
    data = get_summary_data(user)
    if not data:
        raise HTTPException(status_code=404, detail="GitHub user not found")
    
    try:
        insights = analyze_profile(data)
    except Exception as e:
        insights = f"AI Analysis failed: {str(e)}"
    
    return JSONResponse(content={
        "profile": data,
        "insights": insights
    })

# Note: Vercel handles static files via vercel.json, 
# but for local testing, we can mount public directory if it exists
if os.path.isdir("public"):
    app.mount("/", StaticFiles(directory="public", html=True), name="public")
