from flask import Flask, jsonify, request
from dados import alunos

app = Flask(__name__)


@app.route('/aluno', methods=['GET'])
def get_alunos():
    return(jsonify(alunos))


if __name__ == '__main__':
    app.run(debug=False)
