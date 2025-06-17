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
uvicorn main:app --reload
```
Visit: http://127.0.0.1:8000/docs to test.

## Note
🔴 Replace `YOUR_OPENAI_API_KEY` in `review_engine.py`
🔴 Install Node.js & Semgrep CLI for full security support

---