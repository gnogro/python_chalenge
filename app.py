from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/postgres'
db = SQLAlchemy(app)
client_list = []
list_id = str(uuid.uuid4())
counter = 0

class Client(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    celphone = db.Column(db.String(15), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    hash = db.Column(db.String(64), nullable=False)
    list_id = db.Column(db.String(64), nullable=False)

@app.route('/client', methods=['POST'])
def create_client():
    try:
        data = request.get_json()
        global list_id, counter
        if counter > 100:
            counter = 0
        if not all(key in data for key in ['name', 'email', 'celphone', 'status', 'hash']):
            return jsonify({'error': 'Invalid data'}), 422

        counter += 1
        client = Client(
            id=str(uuid.uuid4()),
            name=data['name'],
            email=data['email'],
            celphone=data['celphone'],
            status=data['status'],
            hash=data['hash'],
            list_id=list_id
        )
        
        db.session.add(client)
        client_list.append(client)

        db.session.commit()

        if counter == 100:
            counter = 0
            list_id =str(uuid.uuid4())
            client_list.clear()
            return jsonify({'id': list_id}), 201
        
        return jsonify({'id': list_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/client/<list_id>', methods=['GET'])
def get_client_list(list_id):
    client_list = Client.query.filter_by(list_id=list_id)

    if not client_list:
        return jsonify({'error': 'Client not found'}), 404

    result = {'list': []}

    for client in client_list:
        result['list'].append({
            'id': client.id,
            'name': client.name,
            'email': client.email,
            'celphone': client.celphone,
            'status': client.status,
            'hash': client.hash
        })

    return jsonify(result)

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',port=5000)
