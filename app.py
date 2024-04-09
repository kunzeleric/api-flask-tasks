from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

# create a new task
@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_control
    data = request.get_json()

    new_task = Task(id=task_id_control, title=data['title'], description=data.get('description', ""))
    task_id_control += 1
    tasks.append(new_task)
    return jsonify({ "message": 'New Task created successfully!', "id": new_task.id }), 201

# get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {"tasks": task_list, "total_tasks": len(task_list)}

    return jsonify(output)

# get task by id
@app.route("/tasks/<int:id>", methods=["GET"])
def get_task_by_id(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"message": "Task not found!"}), 404

# update task by id
@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    for t in tasks:
        if t.id == id:
            data = request.get_json()
            t.title = data['title']
            t.description = data.get("description", "")
            t.completed = data.get("completed", False)
            return jsonify(t.to_dict())
    return jsonify({"message": "Task not found!"}), 404

#delete task by id
@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    for t in tasks:
        if t.id == id:
            tasks.remove(t)
            return jsonify({"message": "Task deleted successfully!", "id": id}), 200
    return jsonify({"message": "Task not found!"}), 404

if __name__ == "__main__":
    app.run(debug=True)
