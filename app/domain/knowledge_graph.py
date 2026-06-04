from dataclasses import dataclass, field
from .knowledge_node import KnowledgeNode
from .knowledge_relation import KnowledgeRelation

@dataclass
class KnowledgeGraph:
    nodes_by_id: dict[str, KnowledgeNode] = field(default_factory=dict)
    nodes_by_name: dict[str, KnowledgeNode] = field(default_factory=dict)
    relations: list[KnowledgeRelation] = field(default_factory=list)

    def add_or_update_node(self, name: str, source: str = "", description: str = "") -> KnowledgeNode:
        normalized_name = name.strip().lower()
        if not normalized_name:
            raise ValueError("Le nom du nœud de connaissance ne peut pas être vide.")

        node = self.nodes_by_name.get(normalized_name)

        if node:
            if description and description.strip():
                node.description = description.strip()
            if source and source.strip():
                node.add_source(source.strip())
            return node

        node_id = f"node_{len(self.nodes_by_id) + 1:03d}"
        new_node = KnowledgeNode(id=node_id, name=name, description=description.strip())
        self.nodes_by_id[node_id] = new_node
        self.nodes_by_name[normalized_name] = new_node
        if source:
            new_node.add_source(source.strip())
        return new_node