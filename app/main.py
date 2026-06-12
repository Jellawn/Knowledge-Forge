from ingestion.json_reader import read_json_file
from factories.node_factory import create_node
from mappers.knowledge_node_mapper import node_to_markdown_data
from exporter.markdown_exporter import export_to_markdown, save_markdown_file
from validators.markdown_data_validator import validate_markdown_data
from normalizer.json_node_normalizer import normalize_json_node_data
from domain.knowledge_graph import KnowledgeGraph


nodes = []
raw_data = read_json_file("data/imports/Knowledge2.json")


graph = KnowledgeGraph()
for raw_node_data in raw_data:
    data = normalize_json_node_data(raw_node_data)

    graph.add_or_update_node(
        name=data["name"],
        source=data["sources"][0],
        description=data["description"]
        )

    for relation_data in data["relations"]:
        graph.add_relation(
            source_name=data["name"],
            target_name=relation_data["target"],
            relation_type=relation_data["type"],
            source=data["sources"][0]
        )

print(graph.summarize())