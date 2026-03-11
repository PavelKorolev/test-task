import os
import json

def save_json(input):
    id_obj = input.get("id")
    folder_path = f"projects/{id_obj}" 
    os.makedirs(folder_path, exist_ok=True)
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    version = len(files) + 1

    full_path = os.path.join("projects", f"{id_obj}", f"v{version}.json")

    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(input, f, ensure_ascii=False, indent=4)

    return folder_path