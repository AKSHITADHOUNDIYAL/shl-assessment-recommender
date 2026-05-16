# =========================
# app/services/evaluator.py
# =========================

def recall_at_k(recommended, relevant, k=10):

    recommended_k = recommended[:k]

    relevant_found = len(
        set(recommended_k).intersection(set(relevant))
    )

    return relevant_found / len(relevant)


def groundedness_check(response, catalog_names):

    hallucinations = []

    for word in response.split():

        if "test" in word.lower():
            if word not in catalog_names:
                hallucinations.append(word)

    return hallucinations