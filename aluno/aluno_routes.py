from flask import Blueprint, request, jsonify
from aluno.aluno_model import AlunoNaoEncontrado, get_aluno, get_alunos, create_aluno, update_aluno, delete_aluno


aluno_blueprint = Blueprint('aluno',__name__)


@aluno_blueprint.route('/aluno', methods=['GET'])
def alunos():
    return get_alunos()


@aluno_blueprint.route('/aluno/<int:aluno_id>', methods=['GET'])
def aluno_id(aluno_id):
    try:
        return get_aluno(aluno_id)
    except AlunoNaoEncontrado:
        return jsonify({'mensagem':'aluno não encontrado'}), 404


@aluno_blueprint.route('/aluno', methods=['POST'])
def criar_aluno():
    data = request.json
    create_aluno(data)
    return get_alunos(), 201


@aluno_blueprint.route('/aluno/<int:aluno_id>', methods=['PUT'])
def mudar_aluno(aluno_id):
    data = request.json
    try:
        update_aluno(aluno_id, data)
        return get_aluno(aluno_id), 200
    except AlunoNaoEncontrado:
        return jsonify({'mensagem':"aluno não encontrado"}), 404


@aluno_blueprint.route('/aluno/<int:aluno_id>', methods=['DELETE'])
def excluir_aluno(aluno_id):
    try:
        return delete_aluno(aluno_id)
    except AlunoNaoEncontrado:
        return jsonify({'mensagem':'aluno não encontrado'}), 404