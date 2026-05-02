from flask import Flask, jsonify
import requests

app = Flask(__name__)

USER_SERVICE = "http://127.0.0.1:5002"
PRODUCT_SERVICE = "http://127.0.0.1:5001"


@app.route("/")
def home():
    return jsonify({"gateway": "running", "status": "ok"})


# ---------- USER ROUTE ----------
@app.route("/users", methods=["GET"])
def get_users():
    try:
        res = requests.get(f"{USER_SERVICE}/users")
        return jsonify(res.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------- PRODUCT ROUTE ----------
@app.route("/products", methods=["GET"])
def get_products():
    try:
        res = requests.get(f"{PRODUCT_SERVICE}/products")
        return jsonify(res.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("API GATEWAY RUNNING 🚀")
    app.run(host="0.0.0.0", port=5000, debug=True)