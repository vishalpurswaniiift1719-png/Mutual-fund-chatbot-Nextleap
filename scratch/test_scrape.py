import json

def find_keys(data, target_words, path=""):
    if isinstance(data, dict):
        for k, v in data.items():
            new_path = f"{path}.{k}" if path else k
            if any(w.lower() in k.lower() for w in target_words):
                print(f"Found key: {new_path}")
            find_keys(v, target_words, new_path)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_path = f"{path}[{i}]"
            find_keys(item, target_words, new_path)

with open('scratch/mf_data.json', 'r') as f:
    data = json.load(f)

print("Looking for keys related to our required fields...")
find_keys(data, ["expense", "exit", "sip", "risk", "benchmark", "lock", "category", "fund_name", "scheme_code"])
