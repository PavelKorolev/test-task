import os
import save_json
import json

def versions(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    sorted_files = sorted(files)
    last_versions = sorted_files[-2:]
    v_prev = last_versions[0]
    v_last = last_versions[1]

    path_prev = os.path.join(folder_path, v_prev)
    path_last = os.path.join(folder_path, v_last)

    with open(path_prev, 'r', encoding='utf-8') as f:
        dict1 = json.load(f)

    with open(path_last, 'r', encoding='utf-8') as f:
        dict2 = json.load(f)
    
    common_keys = dict1.keys() & dict2.keys()
    changed = {k: (dict1[k], dict2[k]) for k in common_keys if dict1[k] != dict2[k]}

    return changed


