from get_json import get_json
from structure_control import structure_control
from add_attributes import add_attributes
from save_json import save_json
from versions import versions
import os


def run(data):
    result2 = structure_control(data)
    if result2 is None:
        exit()

    result3 = add_attributes(result2)
    
    result4 = save_json(result3)
    
    if len(os.listdir(result4)) > 1:
        result5 = versions(result4)
    
    print(f"Saved: {result4}")

    return result3


objects = [
    {"name": "Bratislavský hrad", "location": "Bratislava", "year_founded": 907, "country": "Slovakia", "author": "unknown", "condition": "museum", "type": "castle"},
    {"name": "Devín", "location": "Bratislava", "year_founded": 864, "country": "Slovakia", "author": "unknown", "condition": "ruins", "type": "castle"},
    {"name": "Bojnice", "location": "Bojnice", "year_founded": 1113, "country": "Slovakia", "author": "Ján Pálffy", "condition": "museum", "type": "castle"},
    {"name": "Červený Kameň", "location": "Častá", "year_founded": 1240, "country": "Slovakia", "author": "Fugger family", "condition": "museum", "type": "castle"},
    {"name": "Trenčiansky hrad", "location": "Trenčín", "year_founded": 1069, "country": "Slovakia", "author": "unknown", "condition": "partial ruins", "type": "castle"},
    {"name": "Spišský hrad", "location": "Spišské Podhradie", "year_founded": 1209, "country": "Slovakia", "author": "unknown", "condition": "ruins", "type": "castle"},
    {"name": "Oravský hrad", "location": "Oravský Podzámok", "year_founded": 1267, "country": "Slovakia", "author": "unknown", "condition": "museum", "type": "castle"},
    {"name": "Beckov", "location": "Beckov", "year_founded": 1200, "country": "Slovakia", "author": "unknown", "condition": "ruins", "type": "castle"},
    {"name": "Fiľakovo", "location": "Fiľakovo", "year_founded": 1242, "country": "Slovakia", "author": "unknown", "condition": "partial ruins", "type": "castle"},
    {"name": "Krásna Hôrka", "location": "Rožňava", "year_founded": 1320, "country": "Slovakia", "author": "Andrássy family", "condition": "reconstruction", "type": "castle"},
]

objects1 = [
    {"name": "Bratislavský hrad", "location": "Bratislava", "year_founded": 1907, "country": "Slovakia", "author": "unknown", "condition": "museum", "type": "castle"},
    {"name": "Devín", "location": "Bratislava", "year_founded": 1864, "country": "Slovakia", "author": "unknown", "condition": "ruins", "type": "castle"},
    {"name": "Bojnice", "location": "Bojnice", "year_founded": 1113, "country": "Slovakia", "author": "Ján Pálffy", "condition": "museum", "type": "castle"},
    {"name": "Červený Kameň", "location": "Častá", "year_founded": 1240, "country": "Slovakia", "author": "Fugger family", "condition": "museum", "type": "castle"},
    {"name": "Trenčiansky hrad", "location": "Trenčín", "year_founded": 1069, "country": "Slovakia", "author": "unknown", "condition": "partial ruins", "type": "castle"},
    {"name": "Spišský hrad", "location": "Spišské Podhradie", "year_founded": 1209, "country": "Slovakia", "author": "unknown", "condition": "ruins", "type": "castle"},
    {"name": "Oravský hrad", "location": "Oravský Podzámok", "year_founded": 1267, "country": "Slovakia", "author": "unknown", "condition": "museum", "type": "castle"},
    {"name": "Beckov", "location": "Beckov", "year_founded": 1200, "country": "Slovakia", "author": "unknown", "condition": "ruins", "type": "castle"},
    {"name": "Fiľakovo", "location": "Fiľakovo", "year_founded": 1242, "country": "Slovakia", "author": "unknown", "condition": "partial ruins", "type": "castle"},
    {"name": "Krásna Hôrka", "location": "Rožňava", "year_founded": 1320, "country": "Slovakia", "author": "Andrássy family", "condition": "reconstruction", "type": "castle"},
]


saved = []
for obj in objects:
    result = run(obj)
    saved.append(result)
    
for i in [0, 1, 2]:
    updated = objects1[i].copy()
    updated["id"] = saved[i]["id"]
    updated["version"] = saved[i]["version"] 
    run(updated)


v = saved[2]
v = run({**objects1[2], "id": v["id"], "version": v["version"]})
v = run({**objects1[2], "id": v["id"], "version": v["version"]})
v = run({**objects1[2], "id": v["id"], "version": v["version"]})