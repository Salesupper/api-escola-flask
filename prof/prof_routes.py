from flask import Blueprint, request, jsonify
from prof.prof_model import ProfNaoEncontrado, get_prof, get_profs, create_prof, update_prof, delete_prof


prof_blueprint = Blueprint('prof',__name__)


@prof_blueprint.route('/prof', methods=['GET'])
def profs():
    return get_profs()


@prof_blueprint.route('/prof/<int:prof_id>', methods=['GET'])
def prof_id(prof_id):
    try:
        return get_prof(prof_id)
    except ProfNaoEncontrado:
        return jsonify({'mensagem':'professor não encontrado'}), 404


@prof_blueprint.route('/prof', methods=['POST'])
def criar_prof():
    data = request.json
    create_prof(data)
    return get_profs(), 201


@prof_blueprint.route('/prof/<int:prof_id>', methods=['PUT'])
def mudar_prof(prof_id):
    data = request.json
    try:
        update_prof(prof_id, data)
        return get_prof(prof_id), 200
    except ProfNaoEncontrado:
        return jsonify({'mensagem':"professor não encontrado"}), 404


@prof_blueprint.route('/prof/<int:prof_id>', methods=['DELETE'])
def excluir_prof(prof_id):
    try:
        return delete_prof(prof_id)
    except ProfNaoEncontrado:
        return jsonify({'mensagem':'professor não encontrado'}), 404