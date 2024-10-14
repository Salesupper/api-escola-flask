from flask import Blueprint, request, jsonify
import turma.turma_model as tmd


turma_blueprint = Blueprint('turma', __name__) 


@turma_blueprint.route('/turma', methods=['GET'])
def turmas():
    return tmd.get_turmas()
   
   
@turma_blueprint.route('/turma/<int:turma_id>', methods=['GET'])
def turma_id(turma_id):
    try:
        return tmd.get_turma(turma_id)
    except tmd.TurmaNaoEncontrada:
        return jsonify({'mensagem':'turma não encontrada'}), 404


@turma_blueprint.route('/turma', methods=['POST'])
def criar_turma():
    tmd.turma = request.json
    tmd.create_turma()
    return tmd.get_turmas(), 201


@turma_blueprint.route('/turma/<int:turma_id>', methods=['PUT'])
def mudar_turma(turma_id):
    try:
        tmd.data = request.json
        return tmd.update_turma(turma_id)
    except tmd.TurmaNaoEncontrada:
        return jsonify({'mensagem':'turma não encontrada'}), 404


@turma_blueprint.route('/turma/<int:turma_id>', methods=['DELETE'])
def excluir_turma(turma_id):
    try:
        return tmd.delete_turma(turma_id)
    except tmd.TurmaNaoEncontrada:
        return jsonify({'mensagem':'turma não encontrada'}), 404