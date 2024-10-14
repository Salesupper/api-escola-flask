from flask import Blueprint, request, jsonify
import aluno.aluno_model as amd


aluno_blueprint = Blueprint('aluno',__name__)


@aluno_blueprint.route('/aluno', methods=['GET'])
def alunos():
    return amd.get_alunos()


@aluno_blueprint.route('/aluno/<int:aluno_id>', methods=['GET'])
def aluno_id(aluno_id):
    try:
        return amd.get_aluno(aluno_id)
    except amd.AlunoNaoEncontrado:
        return jsonify({'mensagem':'aluno não encontrado'}), 404


@aluno_blueprint.route('/aluno', methods=['POST'])
def criar_aluno():
    amd.aluno = request.json
    amd.create_aluno()
    return amd.get_alunos(), 201


@aluno_blueprint.route('/aluno/<int:aluno_id>', methods=['PUT'])
def mudar_aluno(aluno_id):
    try:
        amd.data = request.json
        return amd.update_aluno(aluno_id)
    except amd.AlunoNaoEncontrado:
        return jsonify({'mensagem':"aluno não encontrado"}), 404


@aluno_blueprint.route('/aluno/<int:aluno_id>', methods=['DELETE'])
def excluir_aluno(aluno_id):
    try:
        return amd.delete_aluno(aluno_id)
    except amd.AlunoNaoEncontrado:
        return jsonify({'mensagem':'aluno não encontrado'}), 404