from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# USERS
@app.route('/users', methods=['GET'])
def get_users():
    res = requests.get("http://localhost:5000/users")
    return jsonify(res.json())

@app.route('/users', methods=['POST'])
def add_user():
    res = requests.post("http://localhost:5000/users", json=request.json)
    return jsonify(res.json())

# PRODUCTS
@app.route('/products', methods=['GET'])
def get_products():
    res = requests.get("http://localhost:5001/products")
    return jsonify(res.json())

@app.route('/products', methods=['POST'])
def add_product():
    res = requests.post("http://localhost:5001/products", json=request.json)
    return jsonify(res.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)