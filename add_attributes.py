import os
import uuid
from datetime import datetime

def add_attributes(input):
    if "id" in input:
         input.update({"version": input.get("version") + 1, 
         "modified_by": os.environ.get("USER", "unknown")})
    else:
        input.update({"id": str(uuid.uuid4()), 
        "version": 1, 
        "created_at": str(datetime.now()), 
        "modified_by": os.environ.get("USER", "unknown")})
        
        
        
    return input