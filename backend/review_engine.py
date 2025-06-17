# review_engine.py

import openai

# Replace with your actual key
client = openai.OpenAI(api_key="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")
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
