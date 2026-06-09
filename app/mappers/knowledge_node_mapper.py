def node_to_markdown_data(node):
    return {
        "title": node.name,
        "summary": node.description,
        "concepts": sorted(node.aliases),
        "examples": []
    }