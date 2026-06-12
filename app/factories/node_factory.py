from domain.knowledge_node import KnowledgeNode

REQUIRED_FIELDS = ["id", "name"]

def create_node(data):
    for field in REQUIRED_FIELDS:
        if field not in data:
            raise KeyError(f"Le champ obligatoire '{field}' est manquant.")

    node = KnowledgeNode(
        id=data["id"],
        name=data["name"],
        description=data.get("description", ""),
    )

    for alias in data.get("aliases", []):
        node.add_alias(alias)

    for source in data.get("sources", []):
        node.add_source(source)

    return node