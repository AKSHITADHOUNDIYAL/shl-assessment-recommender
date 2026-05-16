# =========================
# app/services/comparison_engine.py
# =========================

def compare_assessments(query, retrieved_docs):

    if len(retrieved_docs) < 2:
        return None

    comparison = []

    for doc in retrieved_docs[:2]:

        comparison.append(
            f"""
Name: {doc['name']}
Type: {doc['test_type']}
Description: {doc['description']}
"""
        )

    return "\n".join(comparison)