from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from backend.analyzer import analyze_python_code
#from backend.review_engine import review_code_with_gemini
from backend.review_engine import review_code_with_gpt
from backend.git_utils import get_commit_diff
from backend.feedback_handler import record_feedback
from backend.metrics import compute_complexity
from backend.security_checker import check_security

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class CodeRequest(BaseModel):
    code: str
    language: str
    repo_url: str = None
    pr_id: int = None

class Feedback(BaseModel):
    suggestion_id: str
    decision: str  # accept/reject/modified
    reason: str = None

@app.post("/review")
def review_code(req: CodeRequest):
    static_issues = analyze_python_code(req.code)
    #gemini_review = review_code_with_gemini(req.code)
    gemini_review = review_code_with_gpt(req.code,req.language)
    complexity = compute_complexity(req.code)
    security = check_security(req.code)
    print("Ï am here")
    return {
        "static_issues": static_issues,
        "gemini_review": gemini_review,
        "complexity": complexity,
        "security": security
    }

@app.post("/feedback")
def submit_feedback(fb: Feedback):
    return record_feedback(fb)
