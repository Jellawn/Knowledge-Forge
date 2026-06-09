from domain.knowledge_node import KnowledgeNode
from mappers.knowledge_node_mapper import node_to_markdown_data
from exporter.markdown_exporter import export_to_markdown, save_markdown_file
from validators.markdown_data_validator import validate_markdown_data

node = KnowledgeNode(
        id="gradient_descent",
        name="Gradient Descent",
        description="Algorithme d'optimisation permettant de réduire progressivement une erreur.",
)

node.add_alias("Descente de gradient")
node.add_alias("Gradient")
node.add_alias("Learning Rate")

markdown_data = node_to_markdown_data(node)
validate_markdown_data(markdown_data)
markdown = export_to_markdown(markdown_data)
save_markdown_file(markdown, "exports/gradient_descent.md")