from config import app
from turma.turma_routes import turma_blueprint


app.register_blueprint(turma_blueprint)


if __name__ == '__main__':
    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config["DEBUG"]
    )