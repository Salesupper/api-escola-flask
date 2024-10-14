from flask import Blueprint, request, jsonify
import prof.prof_model as pmd


prof_blueprint = Blueprint('prof',__name__)


@prof_blueprint.route('/prof', methods=['GET'])
def profs():
    return pmd.get_profs()


@prof_blueprint.route('/prof/<int:prof_id>', methods=['GET'])
def prof_id(prof_id):
    try:
        return pmd.get_prof(prof_id)
    except pmd.ProfNaoEncontrado:
        return jsonify({'mensagem':'professor não encontrado'}), 404


@prof_blueprint.route('/prof', methods=['POST'])
def criar_prof():
    pmd.prof = request.json
    pmd.create_prof()
    return pmd.get_profs(), 201


@prof_blueprint.route('/prof/<int:prof_id>', methods=['PUT'])
def mudar_prof(prof_id):
    try:
        pmd.data = request.json
        return pmd.update_prof(prof_id)
    except pmd.ProfNaoEncontrado:
        return jsonify({'mensagem':"professor não encontrado"}), 404


@prof_blueprint.route('/prof/<int:prof_id>', methods=['DELETE'])
def excluir_prof(prof_id):
    try:
        return pmd.delete_prof(prof_id)
    except pmd.ProfNaoEncontrado:
        return jsonify({'mensagem':'professor não encontrado'}), 404