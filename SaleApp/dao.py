import json, os
from SaleApp import app


def read_json(path):
    with open(path, "r", encoding="utf8") as f:
        return json.load(f)


def load_categories():
    return read_json(os.path.join(app.root_path, 'data/categories.json'))


def load_product():
    return read_json(os.path.join(app.root_path, 'data/products.json'))