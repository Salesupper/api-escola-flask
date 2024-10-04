from flask import Flask, jsonify, request
from dados import alunos


def media(n1,n2):
    return (n1+n2)/2


app = Flask(__name__)


@app.route('/aluno', methods=['GET'])
def get_alunos():
    for aluno in alunos:
        if aluno['media'] == None:
            aluno['media'] = media(aluno['nota_b1'], aluno['nota_b2'])
    return(jsonify(alunos))


@app.route('/aluno/<int:aluno_id>', methods=['GET'])
def get_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            return aluno
    return jsonify({'mensagem':'aluno não encontrado'}), 404


@app.route('/aluno', methods=['POST'])
def create_aluno():
    aluno = request.json
    data = {
        'id': len(alunos) + 1,
        'nome': aluno['nome'],
        'idade': aluno['idade'],
        'turma': aluno['turma'],
        'nascimento': aluno['nascimento'],
        'nota_b1':aluno['nota_b1'],
        'nota_b2':aluno['nota_b2'],
        'media': media(aluno['nota_b1'],aluno['nota_b2'])
    }
    alunos.append(data)
    return jsonify(data), 201


@app.route('/aluno/<int:aluno_id>', methods=['PUT'])
def update_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            data = request.json
            aluno['nome'] = data.get('nome', aluno['nome']),
            aluno['idade'] = data.get('idade', aluno['idade']),
            aluno['turma'] = data.get('turma', aluno['turma']),
            aluno['nascimento'] = data.get('nascimento', aluno['nascimento'])
            aluno['nota_b1'] = data.get('nota_b1', aluno['nota_b1']),
            aluno['nota_b2'] = data.get('nota_b2', aluno['nota_b2']),
            aluno['media'] = data.get('media', aluno['media'])
            return jsonify(aluno)
    return jsonify({'mensagem':"aluno não encontrado"}), 404


@app.route('/aluno/<int:aluno_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            alunos.remove(aluno)
            return jsonify({'mensagem':'aluno removido'})
    return jsonify({'mensagem':'aluno não encontrado'}), 404


if __name__ == '__main__':
    app.run(debug=False)
