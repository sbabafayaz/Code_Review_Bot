# review_engine.py

import openai
YOUR_API_KEY = ""
# Replace with your actual key
client = openai.OpenAI(api_key=YOUR_API_KEY)
def review_code_with_gpt(code: str,language:str) -> str:
    prompt =f"""
Review the following {language} code:
- Highlight bugs, design flaws
- Suggest improvements
- Mark severity

Code:
{code}
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a professional code reviewer."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("🔴 OpenAI Error:", e)
        return f"OpenAI Error: {str(e)}"
