import re


COMMON_PASSWORDS = {
    "password",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "welcome",
    "letmein",
    "abc123",
    "password123",
    "iloveyou",
    "000000",
}


def analyze_password(password):

    score = 0
    suggestions = []

    length = len(password)

    # -------------------------
    # Length
    # -------------------------

    if length >= 16:
        score += 30
    elif length >= 12:
        score += 25
    elif length >= 8:
        score += 15
    else:
        suggestions.append("Use at least 8 characters.")

    # -------------------------
    # Uppercase
    # -------------------------

    if re.search(r"[A-Z]", password):
        score += 15
    else:
        suggestions.append("Add at least one uppercase letter.")

    # -------------------------
    # Lowercase
    # -------------------------

    if re.search(r"[a-z]", password):
        score += 15
    else:
        suggestions.append("Add at least one lowercase letter.")

    # -------------------------
    # Number
    # -------------------------

    if re.search(r"\d", password):
        score += 15
    else:
        suggestions.append("Add at least one number.")

    # -------------------------
    # Special character
    # -------------------------

    if re.search(r"[^A-Za-z0-9]", password):
        score += 15
    else:
        suggestions.append("Add a special character such as @, # or $.")

    # -------------------------
    # Common password
    # -------------------------

    if password.lower() in COMMON_PASSWORDS:

        score = min(score, 20)

        suggestions.append(
            "Avoid common or easily guessed passwords."
        )

    # -------------------------
    # Repeated characters
    # -------------------------

    if re.search(r"(.)\1\1", password):

        score -= 10

        suggestions.append(
            "Avoid repeating the same character several times."
        )

    score = max(0, min(score, 100))

    # -------------------------
    # Strength
    # -------------------------

    if score < 40:
        strength = "WEAK"

    elif score < 70:
        strength = "MEDIUM"

    elif score < 90:
        strength = "STRONG"

    else:
        strength = "VERY STRONG"

    return score, strength, suggestions