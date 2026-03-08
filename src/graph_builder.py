import networkx as nx


def build_graph(entities, claims):

    G = nx.DiGraph()

    for e in entities:

        G.add_node(e, type="entity")

    for c in claims:

        G.add_edge(
            c.subject,
            c.object,
            relation=c.relation,
            evidence=c.evidence
        )

    return G