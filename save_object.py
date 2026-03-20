import sys
import os
from get_json import get_json
from structure_control import structure_control
from add_attributes import add_attributes
from save_json import save_json
from versions import versions


if len(sys.argv) < 2:
    print("Usage: python save_object.py input.json")
    exit()

result1 = get_json(sys.argv[1])
if result1 is None:
    exit()

result2 = structure_control(result1)
if result2 is None:
    exit()

result3 = add_attributes(result2)

result4 = save_json(result3)

if len(os.listdir(result4)) > 1:
    result5 = versions(result4)

