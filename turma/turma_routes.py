from flask import Blueprint, request, jsonify
from turma.turma_model import TurmaNaoEncontrada, get_turmas, get_turma, create_turma, update_turma, delete_turma


turma_blueprint = Blueprint('turma', __name__) 


@turma_blueprint.route('/turma', methods=['GET'])
def turmas():
    return jsonify(get_turmas())
   
   
@turma_blueprint.route('/turma/<int:turma_id>', methods=['GET'])
def turma_id(turma_id):
    try:
        turma = get_turma(turma_id)
        return jsonify(turma)
    except TurmaNaoEncontrada:
        return jsonify({'mensagem':'turma não encontrada'}), 404


@turma_blueprint.route('/turma', methods=['POST'])
def criar_turma():
    data = request.json
    create_turma(data)
    return jsonify(data), 201


@turma_blueprint.route('/turma/<int:turma_id>', methods=['PUT'])
def mudar_turma(turma_id):
    data = request.json
    try:
        update_turma(turma_id, data)
        return jsonify(get_turma(turma_id))
    except TurmaNaoEncontrada:
        return jsonify({'mensagem':'turma não encontrada'}), 404


@turma_blueprint.route('/turma/<int:turma_id>', methods=['DELETE'])
def excluir_turma(turma_id):
    try:
        return delete_turma(turma_id)
    except TurmaNaoEncontrada:
        return jsonify({'mensagem':'turma não encontrada'}), 404