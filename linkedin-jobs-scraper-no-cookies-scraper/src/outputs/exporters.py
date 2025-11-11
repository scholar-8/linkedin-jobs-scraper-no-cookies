thonimport json

def export_to_json(data):
    with open('data/sample_output.json', 'w') as f:
        json.dump(data, f, indent=4)