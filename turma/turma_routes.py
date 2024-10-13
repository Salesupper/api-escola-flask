from flask import Blueprint, request, jsonify
from turma.turma_model import *
import turma.turma_model as mdt


turma_blueprint = Blueprint('turma', __name__) 


@turma_blueprint.route('/turma', methods=['GET'])
def turmas():
    return get_turmas()
   
   
@turma_blueprint.route('/turma/<int:turma_id>', methods=['GET'])
def turma_id(turma_id):
    try:
        return get_turma(turma_id)
    except TurmaNaoEncontrada:
        return jsonify({'mensagem':'turma não encontrada'}), 404


@turma_blueprint.route('/turma', methods=['POST'])
def criar_turma():
    mdt.turma = request.json
    create_turma()
    return get_turmas(), 201


@turma_blueprint.route('/turma/<int:turma_id>', methods=['PUT'])
def mudar_turma(turma_id):
    try:
        mdt.data = request.json
        return update_turma(turma_id)
    except TurmaNaoEncontrada:
        return jsonify({'mensagem':'turma não encontrada'}), 404


@turma_blueprint.route('/turma/<int:turma_id>', methods=['DELETE'])
def excluir_turma(turma_id):
    try:
        return delete_turma(turma_id)
    except TurmaNaoEncontrada:
        return jsonify({'mensagem':'turma não encontrada'}), 404
