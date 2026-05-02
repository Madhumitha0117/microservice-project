from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database (resets on restart — expected behavior)
products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Phone", "price": 20000}
]

@app.route('/')
def home():
    return jsonify({
        "service": "Product Service",
        "status": "running"
    })

@app.route('/products', methods=['GET'])
def get_products():
    print("GET /products hit")  # debug log
    return jsonify(products), 200

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON body provided"}), 400

    new_product = {
        "id": len(products) + 1,
        "name": data.get("name"),
        "price": data.get("price")
    }

    products.append(new_product)

    print(f"Product added: {new_product}")  # debug log

    return jsonify(new_product), 201


if __name__ == '__main__':
    print("PRODUCT SERVICE LOADED 🚀")
    app.run(host='0.0.0.0', port=5001, debug=True)