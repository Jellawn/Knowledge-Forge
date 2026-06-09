from pathlib import Path


def export_to_markdown(markdown_data):
        title = markdown_data["title"]
        summary = markdown_data["summary"]
        concepts = markdown_data.get("concepts", [])
        examples = markdown_data.get("examples", [])

        lines = []

        lines.append(f"# {title}")
        lines.append("")

        lines.append("## Résumé")
        lines.append("")
        lines.append(summary)
        lines.append("")

        if concepts:
            lines.append("## Concepts clés")
            lines.append("")
            for concept in concepts:
                lines.append(f"- {concept}")
            lines.append("")

        if examples:
            lines.append("## Exemples")
            lines.append("")
            for example in examples:
                lines.append(f"- {example}")
            lines.append("")

        return "\n".join(lines)

def save_markdown_file(markdown, path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(markdown, encoding="utf-8")


