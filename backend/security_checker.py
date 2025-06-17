import subprocess
import json

def check_security(code: str):
    with open("temp_code.py", "w", encoding="utf-8") as f:
        f.write(code)

    try:
        result = subprocess.run(
            ["semgrep", "--config", "auto", "temp_code.py", "--json"],
            capture_output=True,
            text=True,
            encoding="utf-8"  # ✅ fix for UnicodeDecodeError
        )
        semgrep_output = result.stdout
        findings = json.loads(semgrep_output)
        return findings
    except Exception as e:
        print("🔴 Semgrep Error:", e)
        return {"error": str(e)}
