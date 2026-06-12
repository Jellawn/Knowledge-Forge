from pathlib import Path
import json

def read_json_file(path):
        path = Path(path)
        
        try:
            with path.open("r", encoding="utf-8") as file:
                return json.load(file)

        except FileNotFoundError:
            raise FileNotFoundError(f"Le fichier JSON '{path}' est introuvable.")

        except json.JSONDecodeError:
            raise ValueError(f"Le fichier JSON '{path}' contient un JSON invalide.")