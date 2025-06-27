from flask import Flask, request, jsonify


app = Flask(__name__)
users = { }                             # Dictionary to store users
@app.route('/users', methods=['GET'])
def get_users():                        # gets all users data
    return jsonify(users)           # Returns all users

@app.route('/users/<int:user_id>', methods=['GET'])    # gets a specific user by ID
def get_user(user_id):                                                  
    user = users.get(user_id)
    if user_id in users:
        return jsonify(user[user_id])
    else:
        return jsonify({"message": "User not found"}), 404 
    
@app.route('/users', methods=['POST'])       # adds a new user
def add_user():
    data = request.get_json()      # Get JSON data from request
    name = data.get('name')
    email = data.get('email')
    
    if not name or not email:
        return jsonify({"message": "Name and email are required"}), 400
    new_id = max(users.keys(), default=0) + 1
    users[new_id] = {
        "name": name, "email": email}
    return jsonify({"id": new_id, "message": "User Created Successfully"}), 201
    
@app.route('/users/<int:user_id>', methods=['PUT'])            # updates an existing user
def update_user(user_id):
    if user_id not in users:
        return jsonify({"message": "User {userd_id} not found"}), 404

    data = request.get_json()
    users[user_id]['name'] = data.get('name', users[user_id]['name'])
    users[user_id]['email'] = data.get('email', users[user_id]['email'])
    return jsonify({"message": "User {user_id} updated successfully"}), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])                # deletes a user by ID
def delete_user(user_id):
    if user_id  in users:
        del users[user_id]
        return jsonify({"message": f"User {user_id} deleted successfully"}), 200
    else:
        return jsonify({"message": f"User {user_id} not found"}), 404
    
if __name__ == '__main__':   
    app.run(debug=True)