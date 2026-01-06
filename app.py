from flask import Flask, request, jsonify
from models.tasks import Task

app = Flask(__name__)

# CRUD -> sigla para Create, Read, Update, Delete
# Tabela = Tarefa 

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST']) #rota para o POST (faz parte do CREATE)
def creat_tasks():
    global task_id_control #acessa o valor da variável e não deixa dar erro
    data = request.get_json() #recupera o que o cliente enviar (importado junto com o Flask)
    new_task = Task(id=task_id_control ,title=data.get("title"), description=data.get("description", "")) #serve para recuperar a task
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso"})

@app.route('/tasks', methods=['GET']) # rota para o GET (faz parte do READ)
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    output = {
                "tasks": task_list,
            "total_tasks": len(task_list) #len faz a contagem das atividades
            }
    return jsonify (output)

@app.route('/tasks/<int:id>', methods=['GET']) #pegando a atividade específica pelo id 
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"Não foi possível encontrar a atividade"}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    print(task)
    if task == None:
        return jsonify({"message":"Não foi possível encontrar a atividade"}), 404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify ({"message": "Tarefa atualizada com sucesso"})
#não atualiza o id, porque vou perder o rastreamento dele (vira um novo registro)


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t 
            break
    if not task:
        return jsonify({"message":"Não foi possível encontrar a atividade"}), 404

    tasks.remove(task)
    return jsonify({"message":"Tarefa deletada com sucesso"})


if __name__ == "__main__":
    app.run(debug=True)

