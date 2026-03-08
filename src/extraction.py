import re
from pydantic import BaseModel


class Claim(BaseModel):
    subject: str
    relation: str
    object: str
    evidence: str


def extract_entities(text):

    persons = re.findall(r'[A-Z][a-z]+ [A-Z][a-z]+', text)

    projects = re.findall(r'Project\s[A-Z][a-z]+', text)

    return list(set(persons)), list(set(projects))


def extract_claims(text):

    claims = []

    sentences = text.split(".")

    for sent in sentences:

        if "assigned" in sent:

            claims.append(
                Claim(
                    subject="Unknown",
                    relation="assigned_task",
                    object="Task",
                    evidence=sent
                )
            )

        if "decision" in sent:

            claims.append(
                Claim(
                    subject="Unknown",
                    relation="made_decision",
                    object="Decision",
                    evidence=sent
                )
            )

    return claims