from flask import Flask, jsonify, request
from data import professores

app = Flask(__name__)

@app.route('/prof', methods=['GET'])
def get_profs():
    return jsonify(professores)


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


@app.route('/prof/<int:prof_id>', methods=['GET'])
def get_prof(prof_id):
    for prof in professores:
        if prof['id'] == prof_id:
            return prof
    return jsonify({'mensagem':'usuario não encontrado'}), 404
    



if __name__ == '__main__':
    app.run(debug=True)

