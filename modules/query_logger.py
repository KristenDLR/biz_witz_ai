import os
import json
from datetime import datetime

def log_query(query, response, path="logs/query_log.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True) 
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "query": query,
        "response": response
    }

    try:
        with open(path, "r") as f:
            log = json.load(f)
    except FileNotFoundError:
        log = []

    log.append(entry)

    with open(path, "w") as f:
        json.dump(log, f, indent=2)
