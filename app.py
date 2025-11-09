from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

todos = []
id_counter = 1

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    global id_counter
    data = request.get_json()
    new_todo = {
        "id": id_counter,
        "task": data.get("task", "")
    }
    todos.append(new_todo)
    id_counter += 1
    return jsonify(new_todo)

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    global todos
    todos = [todo for todo in todos if todo["id"] != id]
    return jsonify({"message": "Deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
