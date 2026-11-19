from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Создать репозиторий", "status": "done"},
    {"id": 2, "title": "Написать API", "status": "in_progress"},
]

@app.get("/tasks")
def get_tasks():
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(debug=True)