from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

users = [
    {"id": 1, "name": "Madhu", "role": "student"},
    {"id": 2, "name": "Arjun", "role": "admin"},
    {"id": 3, "name": "Kavya", "role": "developer"},
    {"id": 4, "name": "Ravi", "role": "tester"},
    {"id": 5, "name": "Priya", "role": "designer"},
    {"id": 6, "name": "John", "role": "user"},
    {"id": 7, "name": "Anita", "role": "manager"},
    {"id": 8, "name": "Sara", "role": "analyst"}
]

@app.route("/")
def home():
    return jsonify({
        "service": "User Service",
        "status": "running",
        "version": "1.0"
    })

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({
        "count": len(users),
        "data": users
    })

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json

    new_user = {
        "id": len(users) + 1,
        "name": data.get("name"),
        "role": data.get("role", "user"),
        "created_at": str(datetime.now())
    }

    users.append(new_user)

    return jsonify({
        "message": "User added successfully",
        "user": new_user
    }), 201

if __name__ == "__main__":
    print("USER SERVICE LOADED 🚀")
    app.run(host="0.0.0.0", port=5002, debug=True)