from flask import Flask, jsonify, request
from models import model_turma as mdt


app = Flask(__name__)


####### Turma #######

@app.route('/turma', methods=['GET'])
def turmas():
    return jsonify(mdt.get_turmas())
   
   
@app.route('/turma/<int:turma_id>', methods=['GET'])
def turma_id(turma_id):
    try:
        return jsonify(mdt.get_turma(turma_id))
    except mdt.TurmaNaoEncontrada:
        return jsonify({'erro':'turma não encontrada'}), 404


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
        return jsonify({'erro':'turma não encontrada'}), 404


@app.route('/turma/<int:turma_id>', methods=['DELETE'])
def excluir_turma(turma_id):
    try:
        return jsonify(mdt.delete_turma(turma_id))
    except mdt.TurmaNaoEncontrada:
        return jsonify({'erro':'turma não encontrada'}), 404



if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)