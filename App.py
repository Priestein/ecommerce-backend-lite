from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy in-memory "database"
users = {"admin": "password123"}
products = [{"id": 1, "name": "Laptop", "price": 999}]
cart = []

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if data["username"] in users and users[data["username"]] == data["password"]:
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "fail"}), 401

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/cart", methods=["POST"])
def add_to_cart():
    data = request.json
    cart.append(data)
    return jsonify({"status": "added", "cart": cart})

@app.route("/checkout", methods=["POST"])
def checkout():
    total = sum(item["price"] for item in cart)
    return jsonify({"total": total, "status": "paid"})

if __name__ == "__main__":
    app.run(debug=True)
