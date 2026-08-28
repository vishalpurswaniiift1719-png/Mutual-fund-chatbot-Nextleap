import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

def find_risk(d, path=""):
    if isinstance(d, dict):
        for k, v in d.items():
            if 'risk' in k.lower():
                print(f"Key Match: {path}.{k}")
                if isinstance(v, (str, int, bool)):
                    print(f"  -> {v}")
                elif isinstance(v, dict):
                    # print top level keys of the dict
                    print(f"  -> keys: {list(v.keys())}")
                    
            if isinstance(v, str) and 'risk' in v.lower():
                print(f"Value Match: {path}.{k} -> {v[:100]}")
            find_risk(v, f"{path}.{k}")
    elif isinstance(d, list):
        for i, item in enumerate(d):
            find_risk(item, f"{path}[{i}]")

with open('scratch/mf_data.json', 'r', encoding='utf-8') as f:
    mf_data = json.load(f)

find_risk(mf_data.get('data', {}), "data")
