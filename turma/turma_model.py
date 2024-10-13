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


def create_turma():
    data = {
        'id': len(turmas) + 1,
        'descricao': turma['descricao'],
        'professor': turma['professor'],
        'ativo': turma['ativo']
    }
    turmas.append(data)


def update_turma(turma_id):
    for turma in turmas:
        if turma['id'] == turma_id:
            turma['descricao'] = data.get('descricao', turma['descricao']),
            turma['professor'] = data.get('professor', turma['professor']),
            turma['ativo'] = data.get('ativo', turma['ativo'])
            return turma
    raise TurmaNaoEncontrada


def delete_turma(turma_id):
    for turma in turmas:
        if turma['id'] == turma_id:
            turmas.remove(turma)
            return {'mensagem':'turma removida'}
    raise TurmaNaoEncontrada    


