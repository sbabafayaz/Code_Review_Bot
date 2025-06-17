from radon.complexity import cc_visit

def compute_complexity(code):
    try:
        blocks = cc_visit(code)
        return [{"name": b.name, "complexity": b.complexity} for b in blocks]
    except Exception as e:
        return [{"error": str(e)}]
