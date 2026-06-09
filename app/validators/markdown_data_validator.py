def validate_markdown_data(markdown_data):
    title = markdown_data["title"]
    summary = markdown_data["summary"]

    if not title.strip():
        raise ValueError("Le titre est obligatoire pour exporter en Markdown.")
        
    if not summary.strip():
        raise ValueError("Le résumé est obligatoire pour exporter en Markdown.")
