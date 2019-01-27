import json

def get_categories():
    with open('./output/categories.json') as f:
        data = json.load(f)
        return data['categories']