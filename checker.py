# checker.py
import re

def evaluate_password(password: str) -> dict:
    """Evaluates password strength criteria."""
    return {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\\-]", password)),
    }

def is_strong(checks: dict) -> bool:
    """Returns True if all checks passed, else False."""
    return all(checks.values())
