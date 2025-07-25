from neo4j import GraphDatabase
from .config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

def get_driver():
    return GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def populate_graph(case_id, entities, claims, premises):
    driver = get_driver()
    with driver.session() as session:
        session.write_transaction(_create_case_graph, case_id, entities, claims, premises)
    driver.close()

def _create_case_graph(tx, case_id, entities, claims, premises):
    tx.run("MERGE (c:Case {id: $case_id})", case_id=case_id)
    for ent in entities:
        tx.run("""
            MERGE (e:Entity {text: $text, label: $label})
            MERGE (c:Case {id: $case_id})-[:CONTAINS_ENTITY]->(e)
        """, text=ent["text"], label=ent["label"], case_id=case_id)
    for claim in claims:
        tx.run("""
            MERGE (cl:Claim {text: $claim})
            MERGE (c:Case {id: $case_id})-[:MAKES_CLAIM]->(cl)
        """, claim=claim, case_id=case_id)
    for premise in premises:
        tx.run("""
            MERGE (p:Premise {text: $premise})
            MERGE (c:Case {id: $case_id})-[:HAS_PREMISE]->(p)
        """, premise=premise, case_id=case_id)

def get_case_subgraph(case_id):
    driver = get_driver()
    with driver.session() as session:
        result = session.run("""
            MATCH (c:Case {id: $case_id})-[r]->(n)
            RETURN c, r, n
        """, case_id=case_id)
        nodes, edges = set(), []
        for record in result:
            c = record["c"]
            n = record["n"]
            r = record["r"]
            nodes.add((c.id, "Case"))
            nodes.add((n.id if hasattr(n, "id") else n["text"], n.labels.pop() if hasattr(n, "labels") else n.__class__.__name__))
            edges.append({
                "source": c.id,
                "target": n.id if hasattr(n, "id") else n["text"],
                "type": r.type
            })
        return {
            "nodes": [{"id": nid, "label": label} for nid, label in nodes],
            "edges": edges
        }
    driver.close()
