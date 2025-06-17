import ast
from typing import List, Dict

def analyze_python_code(code: str) -> List[Dict]:
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return [{"line": e.lineno, "issue": "Syntax Error: " + str(e), "severity": "Critical"}]
    issues = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and len(node.name) < 3:
            issues.append({"line": node.lineno, "issue": f"Function name '{node.name}' too short", "severity": "Low"})
    return issues