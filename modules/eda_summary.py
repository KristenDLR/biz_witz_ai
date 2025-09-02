import json

def save_summary_to_json(summary, path="reports/eda_summary.json"):
    with open(path, "w") as f:
        json.dump(summary, f, indent=2)
