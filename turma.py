from flask import Flask, jsonify, request
from dados import turmas


app = Flask(__name__)


@app.route('/turma', methods=['GET'])
def get_turmas():
    return jsonify(turmas)


@app.route('/turma/<int:turma_id>', methods=['GET'])
def get_turma(turma_id):
    for turma in turmas:
        if turma['id'] == turma_id:
            return turma
    return jsonify({'mensagem':'turma não encontrada'}), 404


@app.route('/turma', methods=['POST'])
def create_turma():
    turma = request.json
    data = {
        'id': len(turmas) + 1,
        'descricao': turma['descricao'],
        'professor': turma['professor'],
        'ativo': turma['ativo']
    }
    turmas.append(data)
    return jsonify(data), 201


@app.route('/turma/<int:turma_id>', methods=['PUT'])
def update_turma(turma_id):
    for turma in turmas:
        if turma['id'] == turma_id:
            data = request.json
            turma['descricao'] = data.get('descricao', turma['descricao']),
            turma['professor'] = data.get('professor', turma['professor']),
            turma['ativo'] = data.get('professor', turma['professor'])
            return jsonify(turma)
    return jsonify({'mensagem':'turma não encontrada'}), 404


@app.route('/turma/<int:turma_id>', methods=['DELETE'])
def delete_turma(turma_id):
    for turma in turmas:
        if turma['id'] == turma_id:
            turmas.remove(turma)
            return jsonify({'mensagem':'turma removida'})
    return jsonify({'mensagem':'turma não encontrada'}), 404    


if __name__ == '__main__':
    app.run(debug=False)