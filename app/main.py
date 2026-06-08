from domain.knowledge_graph import KnowledgeGraph


def build_learning_graph() -> KnowledgeGraph:
    graph = KnowledgeGraph()

    graph.add_relation( source_name="Machine Learning",
                        relation_type="utilise",
                        target_name="Algèbre Linéaire",
                        source="roadmap_ml.md"
                       )

    graph.add_relation( source_name="Machine Learning",
                        relation_type="utilise",
                        target_name="Probabilités",
                        source="roadmap_ml.md"
                       )

    graph.add_relation( source_name="Machine Learning",
                        relation_type="utilise",
                        target_name="Algèbre Linéaire",
                        source="cours_ml.md"
                       )

    return graph

if __name__ == "__main__":
        learning_graph = build_learning_graph()
        print(learning_graph.summarize())