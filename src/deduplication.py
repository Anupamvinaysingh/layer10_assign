import hashlib


def hash_text(text):

    return hashlib.sha256(text.encode()).hexdigest()


def deduplicate_entities(entity_list):

    seen = set()
    unique = []

    for e in entity_list:

        if e.lower() not in seen:
            seen.add(e.lower())
            unique.append(e)

    return unique


def deduplicate_claims(claims):

    seen = set()
    unique = []

    for c in claims:

        key = hash_text(c.subject + c.relation + c.object)

        if key not in seen:
            seen.add(key)
            unique.append(c)

    return unique