import os
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Lista exata dos 20 usuários exigidos
EXACT_CODES = [
    'C910',
    'C920',
    'C930',
    'C940',
    'C950',
    'C960',
    'C970',
    'C980',
    'C990',
    'C1000',
    'C911',
    'C921',
    'C931',
    'C941',
    'C951',
    'C961',
    'C971',
    'C981',
    'C991',
    'C1001',
]

# Base de dados em memória para o protótipo
users_db = [
    {'id': code, 'aluminio': 0.0, 'pet': 0.0, 'papel': 0.0}
    for code in EXACT_CODES
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users_db)


@app.route('/api/users/<user_id>', methods=['PUT'])
def update_user_weight(user_id):
    data = request.get_json()
    for user in users_db:
        if user['id'] == user_id:
            if 'aluminio' in data:
                user['aluminio'] = float(data['aluminio'])
            if 'pet' in data:
                user['pet'] = float(data['pet'])
            if 'papel' in data:
                user['papel'] = float(data['papel'])
            return jsonify({'status': 'success', 'user': user})
    return jsonify({'status': 'error', 'message': 'Usuário não encontrado'}), 404


@app.route('/api/reset', methods=['POST'])
def reset_data():
    global users_db
    users_db = [
        {'id': code, 'aluminio': 0.0, 'pet': 0.0, 'papel': 0.0}
        for code in EXACT_CODES
    ]
    return jsonify({'status': 'success', 'users': users_db})


# ==========================================
# INICIALIZAÇÃO COMPATÍVEL COM O RENDER
# ==========================================
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)