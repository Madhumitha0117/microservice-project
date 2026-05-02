from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Madhu", "role": "student"},
    {"id": 2, "name": "Guest", "role": "user"}
]

@app.route("/")
def home():
    return jsonify({
        "service": "User Service",
        "status": "running"
    })

@app.route("/users", methods=["GET"])
def get_users():
    print("GET /users hit")
    return jsonify(users), 200


@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON body"}), 400

    new_user = {
        "id": len(users) + 1,
        "name": data.get("name"),
        "role": data.get("role", "user")
    }

    users.append(new_user)

    print(f"User added: {new_user}")

    return jsonify(new_user), 201


if __name__ == "__main__":
    print("USER SERVICE LOADED 🚀")
    app.run(host="0.0.0.0", port=5002, debug=True)