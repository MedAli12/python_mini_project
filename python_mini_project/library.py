import json


def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)


def add_item(item, file_name):
    data = load_data(file_name)
    data.append(item)
    save_data(data, file_name)


def find_item_index(item_id, items):
    for index, item in enumerate(items):
        if 'id' in item and item['id'] == item_id:
            return index
    return -1


def modify_item(item_id, item, file_name):
    data = load_data(file_name)
    index = find_item_index(item_id, data)
    if index is not None:
        data[index] = item
        save_data(data, file_name)
    else:
        raise ValueError("Item not found")


def delete_item(item_id, file_name):
    data = load_data(file_name)
    index = find_item_index(item_id, data)
    if index is not None:
        del data[index]
        save_data(data, file_name)
    else:
        raise ValueError("Item not found")
