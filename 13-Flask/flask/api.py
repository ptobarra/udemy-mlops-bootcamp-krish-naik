### Put and Delete - HTTP Verbs
### Working with API's - JSON


from flask import Flask, jsonify, request

app = Flask(__name__)

## Initial Data in my todo list
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
]


@app.route("/")
def home():
    return "Welcome to the sample TODO list App."


## Get: Retrieve all the items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)


## GET: Retrieve a specific item by id
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "item not found"}), 404
    return jsonify(item)


## POST: create a new task - API
@app.route("/items", methods=["POST"])
def create_item():
    if not request.json or "name" not in request.json:
        return jsonify({"error": "item not found"}), 400

    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json["name"],
        "description": request.json["description"],
    }

    items.append(new_item)
    return jsonify(new_item), 201


## PUT: update an existing item
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "item not found"}), 404

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "request must be JSON"}), 400

    # item["name"] = request.json.get("name", item["name"])
    item["name"] = data.get("name", item["name"])
    # item["description"] = request.json.get("description", item["description"])
    item["description"] = data.get("description", item["description"])
    return jsonify(item)


## DELETE: Delete an item
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items
    items = [i for i in items if i["id"] != item_id]
    return jsonify({"result": "Item deleted"})


if __name__ == "__main__":
    app.run(debug=True)
