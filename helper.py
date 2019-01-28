import json

def get_categories():
    with open('./output/categories.json') as f:
        data = json.load(f)
        return data['categories']

def get_all_questions(file_path):
        with open(file_path) as f:
                data = json.load(f)
                return data['questions']
