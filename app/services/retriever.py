# =========================
# app/services/retriever.py
# =========================

import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/shl_catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

documents = [
    f"{item['name']} {item['description']} {item['test_type']}"
    for item in catalog
]

embeddings = model.encode(documents)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings).astype("float32"))


def retrieve_assessments(query, top_k=5):

    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        top_k
    )

    results = []

    for idx in indices[0]:
        results.append(catalog[idx])

    return results