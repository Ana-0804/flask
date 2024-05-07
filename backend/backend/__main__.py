from flask import jsonify,Response , request
from backend import create_app

app =create_app()

@app.route('/health', methods = ["GET"])
def Health_check():
    return 'ok'

@app.route('/users', methods =["GET"])
def get_all_users() :
         all_users = [{'id' : 1 , "name": "Ana"} , {'id': 2 , "name" : "Ani"}]
         return jsonify({'Users' : all_users})
@app.route('/users', methods=["POST"])
def add_user():
      name = request.json['name']
      id   = request.json['id'] if 'id' in request.json else None
      user={'name': name}
      if id:
          user['id'] = id
      app.users.add_user(user)
      return jsonify(user), 201

if __name__ == '__main__':
    app.run(host ='127.0.0.1') 
