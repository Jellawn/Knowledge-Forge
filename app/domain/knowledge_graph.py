from dataclasses import dataclass, field
from .knowledge_node import KnowledgeNode
from .knowledge_relation import KnowledgeRelation

@dataclass
class KnowledgeGraph:
    nodes_by_id: dict[str, KnowledgeNode] = field(default_factory=dict)
    nodes_by_name: dict[str, KnowledgeNode] = field(default_factory=dict)
    relations: list[KnowledgeRelation] = field(default_factory=list)
    

    def add_or_update_node(self, name: str, source: str, description: str = "") -> KnowledgeNode:
        normalized_name = name.strip().lower()

        if not normalized_name:
           raise ValueError("Le nom du nœud de connaissance ne peut pas être vide.")

        node = self.nodes_by_name.get(normalized_name)

        if node:
                if description and description.strip():
                 node.description = description.strip()

                node.add_source(source)
                return node

        node_id = f"node_{len(self.nodes_by_id) + 1:03d}"
        new_node = KnowledgeNode(id=node_id, name=name.strip(), description=description.strip())
        new_node.add_source(source)

        self.nodes_by_id[node_id] = new_node
        self.nodes_by_name[normalized_name] = new_node

        return new_node

    def add_relation(self, source_name: str, target_name: str, relation_type: str, source: str,) -> KnowledgeRelation:
       source_node = self.add_or_update_node(source_name, source)
       target_node = self.add_or_update_node(target_name, source)
       normalized_relation_type = relation_type.strip().lower()

       for relation in self.relations:
           if (relation.source_node_id == source_node.id and
               relation.target_node_id == target_node.id and
               relation.relation_type == normalized_relation_type):
               relation.add_source(source)
               return relation

       relation_id = f"relation_{len(self.relations) + 1:03d}"
       new_relation = KnowledgeRelation(
            id=relation_id,
            source_node_id=source_node.id,
            target_node_id=target_node.id,
            relation_type=normalized_relation_type,
        )
       new_relation.add_source(source)
       self.relations.append(new_relation)
       return new_relation

    def summarize(self) -> str:
        lines = []

        lines.append("Knowledge Graph Summary:")
        lines.append(f"Total Nodes: {len(self.nodes_by_id)}")
        lines.append(f"Total Relations: {len(self.relations)}")
        
        lines.append("\nNodes:")
        for node in self.nodes_by_id.values():
            lines.append(f"- {node.name} (ID: {node.id}, Sources: {node.source_count})")

        lines.append("\nRelations:")
        for relation in self.relations:
            source_node = self.nodes_by_id[relation.source_node_id]
            target_node = self.nodes_by_id[relation.target_node_id]

            lines.append(f"- {source_node.name} --[{relation.relation_type}]--> {target_node.name} | Sources: {relation.source_count})")

        return "\n".join(lines)