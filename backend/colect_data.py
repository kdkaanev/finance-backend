import json

# Open and read the JSON file
category = set()
with open('data/data.json', 'r') as f:
    data = json.load(f)


for key, value in data.items():
    if key == 'transactions':
        for transaction in value:
            category.add(transaction['category'])
category_list = [cat for cat in category]
print(category_list)
with open('data/category.json', 'w') as f:
    json.dump(category_list, f)