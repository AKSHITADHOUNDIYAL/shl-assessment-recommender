# =========================
# app/services/guardrails.py
# =========================

FORBIDDEN_TOPICS = [
    "legal advice",
    "medical advice",
    "ignore previous instructions",
    "hack",
    "bypass"
]


def is_off_topic(query):

    query = query.lower()

    for topic in FORBIDDEN_TOPICS:
        if topic in query:
            return True

    return False