from config import db


class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(5), nullable=False)
    professor = db.Column(db.Integer, nullable=False)
    ativo = db.Column(db.Boolean, default=True)

    def __init__(self, descricao, professor, ativo):
        self.descricao = descricao
        self.professor = professor
        self.ativo = ativo

    def to_dict(self):
        return {
            'id': self.id, 
            'descricao': self.descricao, 
            'professor': self.professor,
            'ativo': self.ativo
        }


class TurmaNaoEncontrada(Exception):
    pass


def get_turmas():
    turmas = Turma.query.all()
    return [turma.to_dict() for turma in turmas]


def get_turma(turma_id):
    turma = Turma.query.get(turma_id)
    if not turma:
        raise TurmaNaoEncontrada
    return turma.to_dict()


def create_turma(data):
    nova_turma = Turma(
        descricao = data['descricao'],
        professor = data['professor'],
        ativo = data['ativo']
    )
    db.session.add(nova_turma)
    db.session.commit()


def update_turma(turma_id, data):
    turma = Turma.query.get(turma_id)
    if not turma:
        raise TurmaNaoEncontrada
    turma.descricao = data['descricao']
    turma.professor = data['professor']
    turma.ativo = data['ativo']
    db.session.commit()


def delete_turma(turma_id):
    turma = Turma.query.get(turma_id)
    if not turma:
        raise TurmaNaoEncontrada
    db.session.delete(turma)
    db.session.commit()
    


