from dataclasses import dataclass, field

@dataclass
class KnowledgeNode:
    id: str
    name: str
    description: str = ""
    aliases: set[str] = field(default_factory=set)
    sources: set[str] = field(default_factory=set)

    @property
    def source_count(self) -> int:
        return len(self.sources)

    def __post_init__(self) -> None:
        if not self.id.strip():
                raise ValueError("L'identifiant du nœud de connaissance ne peut pas être vide.")

        if not self.name.strip():
                raise ValueError("Le nom du nœud de connaissance ne peut pas être vide.")

    def add_source(self, source: str) -> None:
        if not source.strip():
                raise ValueError("La source ne peut pas être vide.")

        self.sources.add(source.strip())


    def add_alias(self, alias: str) -> None:
        if not alias.strip():
                raise ValueError("L'alias ne peut pas être vide.")

        self.aliases.add(alias.strip())