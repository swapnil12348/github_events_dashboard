import json
import os

def load_data():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Loaded {len(data)} events from data.json")
        return data
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return []

def save_data(data):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data.json')
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)