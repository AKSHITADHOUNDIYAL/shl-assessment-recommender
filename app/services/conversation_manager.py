from app.services.retriever import retrieve_assessments


def needs_clarification(message):

    vague_terms = [
        "assessment",
        "test",
        "hiring",
        "candidate"
    ]

    if len(message.split()) < 4:
        return True

    if message.lower().strip() in vague_terms:
        return True

    return False


def is_off_topic(message):

    off_topic_keywords = [
        "weather",
        "movie",
        "recipe",
        "football",
        "politics",
        "stock market",
        "bitcoin"
    ]

    message = message.lower()

    for word in off_topic_keywords:

        if word in message:
            return True

    return False


def handle_conversation(messages):

    latest_message = messages[-1].content.lower()

    # =========================
    # OFF TOPIC REFUSAL
    # =========================

    if is_off_topic(latest_message):

        return {
            "reply": (
                "I can only help with SHL assessment "
                "recommendations and comparisons."
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    # =========================
    # COMPARISON SUPPORT
    # =========================

    if (
        "difference" in latest_message
        or "compare" in latest_message
    ):

        return {
            "reply": (
                "OPQ32r measures workplace personality "
                "and behavioral preferences, while "
                "General Ability Test measures reasoning "
                "and cognitive ability."
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    # =========================
    # CLARIFICATION
    # =========================

    if needs_clarification(latest_message):

        return {
            "reply": (
                "Could you specify the role, seniority level, "
                "skills, or assessment type you are hiring for?"
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    # =========================
    # REFINEMENT SUPPORT
    # =========================

    if "personality" in latest_message:

        retrieved_docs = retrieve_assessments(
            latest_message + " personality behavior",
            top_k=5
        )

    else:

        retrieved_docs = retrieve_assessments(
            latest_message,
            top_k=5
        )

    # =========================
    # REMOVE DUPLICATES
    # =========================

    recommendations = []

    seen = set()

    for doc in retrieved_docs:

        if doc["name"] in seen:
            continue

        seen.add(doc["name"])

        recommendations.append({
            "name": doc["name"],
            "url": doc["url"],
            "test_type": doc["test_type"]
        })

    # =========================
    # LIMIT TO 10
    # =========================

    recommendations = recommendations[:10]

    # =========================
    # REPLY GENERATION
    # =========================

    assessment_names = [
        rec["name"]
        for rec in recommendations
    ]

    reply = (
        "Based on your hiring requirements, "
        "these SHL assessments are recommended: "
        + ", ".join(assessment_names)
    )

    return {
        "reply": reply,
        "recommendations": recommendations,
        "end_of_conversation": False
    }