from config import app, db
from turma.turma_routes import turma_blueprint
from prof.prof_routes import prof_blueprint
from aluno.aluno_routes import aluno_blueprint


app.register_blueprint(turma_blueprint)
app.register_blueprint(prof_blueprint)
app.register_blueprint(aluno_blueprint)

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(
        host = app.config["HOST"],
        port = app.config["PORT"],
        debug = app.config["DEBUG"]
    )