from flask import Flask, jsonify, request
from dados import professores

app = Flask(__name__)


@app.route('/prof', methods=['GET'])
def get_profs():
    return jsonify(professores)


@app.route('/prof/<int:prof_id>', methods=['GET'])
def get_prof(prof_id):
    for prof in professores:
        if prof['id'] == prof_id:
            return prof
    return jsonify({'mensagem':'usuario não encontrado'}), 404


@app.route('/prof', methods=['POST'])
def create_prof():
    prof = request.json
    professor = {
        'id': len(professores) + 1,
        'nome': prof['nome'],
        'idade': prof['idade'],
        'materia': prof['materia'],
        'observacoes': prof['observacoes']
    }
    professores.append(professor)
    return jsonify(professor), 201


@app.route('/prof/<int:prof_id>', methods=['PUT'])
def update_prof(prof_id):
    for prof in professores:
        if prof['id'] == prof_id:
            data = request.json
            prof['nome'] = data.get('nome', prof['nome']),
            prof['idade'] = data.get('idade', prof['idade']),
            prof['materia'] = data.get('materia', prof['materia']),
            prof['observacoes'] = data.get('observacoes', prof['observacoes'])
            return jsonify(prof)
    return jsonify({'mensagem':"professor não encontrado"}), 404


@app.route('/prof/<int:prof_id>', methods=['DELETE'])
def delete_prof(prof_id):
    for prof in professores:
        if prof['id'] == prof_id:
            professores.remove(prof)
            return jsonify({'mensagem':'professor removido'})
    return jsonify({'mensagem':'professor não encontrado'}), 404


if __name__ == '__main__':
    app.run(debug=True)

