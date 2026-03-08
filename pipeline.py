from src.preprocess import load_emails
from src.extraction import extract_entities, extract_claims
from src.deduplication import deduplicate_entities, deduplicate_claims
from src.graph_builder import build_graph
from src.retrieval import retrieve
import json


dataset_path = "data/maildir"

df = load_emails(dataset_path)

all_entities = []
all_claims = []


for _, row in df.iterrows():

    body = str(row["body"])

    persons, projects = extract_entities(body)

    claims = extract_claims(body)

    all_entities.extend(persons)
    all_entities.extend(projects)

    all_claims.extend(claims)


entities = deduplicate_entities(all_entities)

claims = deduplicate_claims(all_claims)


G = build_graph(entities, claims)


with open("outputs/entities.json", "w") as f:

    json.dump(entities, f)


with open("outputs/claims.json", "w") as f:

    json.dump([c.dict() for c in claims], f)


print("Graph built successfully")
print("Entities:", len(entities))
print("Claims:", len(claims))


# test retrieval

question = "Who assigned the task?"

results = retrieve(question, claims)

for score, claim in results:

    print(score, claim)