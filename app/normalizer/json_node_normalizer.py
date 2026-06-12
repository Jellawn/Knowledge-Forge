REQUIRED_FIELDS = ["node_id", "node_title"]

def normalize_json_node_data(raw_data):
    
    for field in REQUIRED_FIELDS:
        if field not in raw_data:
            raise KeyError(f"Le champ obligatoire '{field}' est manquant dans les données JSON.")
    
    return {
        "id": raw_data["node_id"],
        "name": raw_data["node_title"],
        "description": raw_data.get("summary", ""),
        "aliases": raw_data.get("keywords", []),
        "sources": raw_data.get("references", []),
        "relations": raw_data.get("relations", [])
    }