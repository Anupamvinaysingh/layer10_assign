from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


def embed(text):

    return model.encode(text)


def retrieve(question, claims):

    q_vec = embed(question)

    best = []

    for c in claims:

        text = f"{c.subject} {c.relation} {c.object}"

        vec = embed(text)

        sim = np.dot(q_vec, vec)

        best.append((sim, c))

    best.sort(reverse=True)

    return best[:5]