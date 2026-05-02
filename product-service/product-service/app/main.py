from flask import Flask, jsonify, request

app = Flask(__name__)

products = []

@app.route('/')
def home():
    return jsonify({"service": "Product Service", "status": "running"})

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json

    product = {
        "id": len(products) + 1,
        "name": data.get("name"),
        "price": data.get("price")
    }

    products.append(product)
    return jsonify(product), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)