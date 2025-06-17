# Code Review Bot

## Features
- Gemini-based intelligent suggestions
- Static analysis via AST
- Complexity scoring
- Git PR diff analysis
- Feedback loop and database
- Security scanning via Bandit + Semgrep
## API_KEY
 - Please change the API key at ..\backend\review_engine.py
## How to Run
 - Run both in different Terminals
```bash
cd Code_Review_Bot

# Frontend Setup
cd frontend
npm install
npm run dev

# Backend Setup

cd backend
python -m venv venv
venv\Scripts\activate      # Use `source venv/bin/activate` on Mac/Linux
pip install -r ../requirements.txt  
uvicorn main:app --reload
