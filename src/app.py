from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [ 
   { "label": "My first task", "done": False, "id": 6 },
    { "label": "My second task", "done": False, "id": 7 }
  ]

@app.route('/todos', methods=['POST']) #crear endpoint
def add_new_todo():
    
    request_body = request.get_json(force=True)
    todos.append(request_body) # inserta el nuevo miembro con APPEND
    todolist = jsonify(todos)
    print("Incoming request with the following body", request_body)
    return todolist
   


@app.route('/todos', methods=['GET'])
def get_todo():

  return jsonify(todos)



@app.route('/todos/<int:id>', methods=['GET'])
def get_todo_id(id):
   
   int_id = list(filter(lambda todo: todo['id'] == id, todos)) 
   print(int_id)
   return 'response from todo id'



@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    
    print("This is the position to delete:", position)
    todos.pop(position)
    return jsonify(todos)
   


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)