from dados import turmas


class TurmaNaoEncontrada(Exception):
    pass


def get_turmas():
    return turmas


def get_turma(turma_id):
    for turma in turmas:
        if turma['id'] == turma_id:
            return turma
    raise TurmaNaoEncontrada


def create_turma(data):
    turma = {
        'id': len(turmas) + 1,
        'descricao': data['descricao'],
        'professor': data['professor'],
        'ativo': data['ativo']
    }
    turmas.append(turma)


def update_turma(turma_id, data):
    turma = get_turma(turma_id)
    t = {
        'id': turma_id,
        'descricao': data['descricao'],
        'professor': data['professor'],
        'ativo': data['ativo']
    }
    turma.update(t)


def delete_turma(turma_id):
    turma = get_turma(turma_id)
    turmas.remove(turma)
    return {'mensagem':'turma removida'}
    


