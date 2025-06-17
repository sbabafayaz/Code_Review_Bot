# Code Review Bot

## Features
- Gemini-based intelligent suggestions
- Static analysis via AST
- Complexity scoring
- Git PR diff analysis
- Feedback loop and database
- Security scanning via Bandit + Semgrep

## How to Run

```bash
# Frontend Setup
cd frontend
npm install
npm run dev

# Backend Setup
```bash
cd ../backend
python -m venv venv
venv\Scripts\activate      # Use `source venv/bin/activate` on Mac/Linux
pip install -r ../requirements.txt  # requirements.txt is in the root directory
uvicorn main:app --reload
