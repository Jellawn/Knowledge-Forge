from app.domain.knowledge_node import KnowledgeNode



node = KnowledgeNode(
        id="node_001",
        name="Gradient Descent",
        description="Algorithme d'optimisation permettant de minimiser une fonction de coût.",
)

node.sources.add("document_A")
node.sources.add("document_B")
node.sources.add("document_A")

print(node)
print(node.source_count)
