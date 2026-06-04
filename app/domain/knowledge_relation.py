from dataclasses import dataclass, field


@dataclass
class KnowledgeRelation:
    id: str
    source_node_id: str
    target_node_id: str
    relation_type: str
    description: str = ""
    sources: set[str] = field(default_factory=set)

    @property
    def source_count(self) -> int:
        return len(self.sources)

    def __post_init__(self) -> None:
        if not self.id.strip():
            raise ValueError("L'identifiant de la relation de connaissance ne peut pas être vide.")

        if not self.source_node_id.strip():
            raise ValueError("L'identifiant du nœud source ne peut pas être vide.")

        if not self.target_node_id.strip():
            raise ValueError("L'identifiant du nœud cible ne peut pas être vide.")

        if not self.relation_type.strip():
            raise ValueError("Le type de relation ne peut pas être vide.")

        self.relation_type = self.relation_type.strip().lower()

    def add_source(self, source: str) -> None:
        if not source.strip():
            raise ValueError("La source ne peut pas être vide.")

        self.sources.add(source.strip())