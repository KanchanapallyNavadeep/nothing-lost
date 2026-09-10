import json
import os


DATA_FILE = os.path.join(
    os.path.dirname(__file__),
    "data.json"
)


def load_data():

    if not os.path.exists(DATA_FILE):
        return {
            "lost_items": [],
            "found_items": []
        }

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_data(data):

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4
        )


def add_lost_item(item):

    data = load_data()

    data["lost_items"].append(item)

    save_data(data)


def add_found_item(item):

    data = load_data()

    data["found_items"].append(item)

    save_data(data)
    