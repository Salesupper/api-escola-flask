from flask import Flask, jsonify, request
from dados import turmas

app = Flask(__name__)

@app.route('/turma')
def get_turmas():
    return jsonify(turmas)


if __name__ == '__main__':
    app.run(debug=False)