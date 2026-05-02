from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 50000, "category": "Electronics"},
    {"id": 2, "name": "Smartphone", "price": 20000, "category": "Electronics"},
    {"id": 3, "name": "Headphones", "price": 3000, "category": "Accessories"},
    {"id": 4, "name": "Keyboard", "price": 1500, "category": "Accessories"},
    {"id": 5, "name": "Mouse", "price": 800, "category": "Accessories"},
    {"id": 6, "name": "Monitor", "price": 12000, "category": "Electronics"},
    {"id": 7, "name": "Tablet", "price": 25000, "category": "Electronics"},
    {"id": 8, "name": "Smartwatch", "price": 5000, "category": "Wearables"},
    {"id": 9, "name": "Charger", "price": 700, "category": "Accessories"},
    {"id": 10, "name": "USB Cable", "price": 300, "category": "Accessories"}
]

@app.route("/")
def home():
    return jsonify({
        "service": "Product Service",
        "status": "running",
        "version": "1.0"
    })

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify({
        "count": len(products),
        "data": products
    })

@app.route("/products", methods=["POST"])
def add_product():
    data = request.json

    new_product = {
        "id": len(products) + 1,
        "name": data.get("name"),
        "price": data.get("price"),
        "category": data.get("category", "General"),
        "created_at": str(datetime.now())
    }

    products.append(new_product)

    return jsonify({
        "message": "Product added successfully",
        "product": new_product
    }), 201

if __name__ == "__main__":
    print("PRODUCT SERVICE LOADED 🚀")
    app.run(host="0.0.0.0", port=5001, debug=True)