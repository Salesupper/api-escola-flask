from flask import Flask, jsonify, request
from models import model_turma as mdt
from models import model_prof as mdp
from models import model_aluno as mda


app = Flask(__name__)


####### Turmas #######

@app.route('/turma', methods=['GET'])
def turmas():
    return mdt.get_turmas()
   
   
@app.route('/turma/<int:turma_id>', methods=['GET'])
def turma_id(turma_id):
    try:
        return mdt.get_turma(turma_id)
    except mdt.TurmaNaoEncontrada:
        return jsonify({'mensagem':'turma não encontrada'}), 404


@app.route('/turma', methods=['POST'])
def criar_turma():
    mdt.turma = request.json
    mdt.create_turma()
    return mdt.get_turmas(), 201


@app.route('/turma/<int:turma_id>', methods=['PUT'])
def mudar_turma(turma_id):
    try:
        mdt.data = request.json
        return mdt.update_turma(turma_id)
    except mdt.TurmaNaoEncontrada:
        return jsonify({'mensagem':'turma não encontrada'}), 404


@app.route('/turma/<int:turma_id>', methods=['DELETE'])
def excluir_turma(turma_id):
    try:
        return mdt.delete_turma(turma_id)
    except mdt.TurmaNaoEncontrada:
        return jsonify({'mensagem':'turma não encontrada'}), 404


####### Profs #######

@app.route('/prof', methods=['GET'])
def profs():
    return mdp.get_profs()


@app.route('/prof/<int:prof_id>', methods=['GET'])
def prof_id(prof_id):
    try:
        return mdp.get_prof(prof_id)
    except mdp.ProfNaoEncontrado:
        return jsonify({'mensagem':'professor não encontrado'}), 404


@app.route('/prof', methods=['POST'])
def criar_prof():
    mdp.prof = request.json
    mdp.create_prof()
    return mdp.get_profs(), 201


@app.route('/prof/<int:prof_id>', methods=['PUT'])
def mudar_prof(prof_id):
    try:
        mdp.data = request.json
        return mdp.update_prof(prof_id)
    except mdp.ProfNaoEncontrado:
        return jsonify({'mensagem':"professor não encontrado"}), 404


@app.route('/prof/<int:prof_id>', methods=['DELETE'])
def excluir_prof(prof_id):
    try:
        return mdp.delete_prof(prof_id)
    except mdp.ProfNaoEncontrado:
        return jsonify({'mensagem':'professor não encontrado'}), 404


####### Alunos #######

@app.route('/aluno', methods=['GET'])
def alunos():
    return mda.get_alunos()


@app.route('/aluno/<int:aluno_id>', methods=['GET'])
def aluno_id(aluno_id):
    try:
        return mda.get_aluno(aluno_id)
    except mda.AlunoNaoEncontrado:
        return jsonify({'mensagem':'aluno não encontrado'}), 404


@app.route('/aluno', methods=['POST'])
def criar_aluno():
    mda.aluno = request.json
    mda.create_aluno()
    return mda.get_alunos(), 201


@app.route('/aluno/<int:aluno_id>', methods=['PUT'])
def mudar_aluno(aluno_id):
    try:
        mda.data = request.json
        return mda.update_aluno(aluno_id)
    except mda.AlunoNaoEncontrado:
        return jsonify({'mensagem':"aluno não encontrado"}), 404


@app.route('/aluno/<int:aluno_id>', methods=['DELETE'])
def excluir_aluno(aluno_id):
    try:
        return mda.delete_aluno(aluno_id)
    except mda.AlunoNaoEncontrado:
        return jsonify({'mensagem':'aluno não encontrado'}), 404



if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)

