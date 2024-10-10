from dados import professores


class ProfNaoEncontrado(Exception):
    pass


def get_profs():
    return professores


def get_prof(prof_id):
    for prof in professores:
        if prof['id'] == prof_id:
            return prof
    raise ProfNaoEncontrado


def create_prof():
    data = {
        'id': len(professores) + 1,
        'nome': prof['nome'],
        'idade': prof['idade'],
        'materia': prof['materia'],
        'observacoes': prof['observacoes']
    }
    professores.append(data)


def update_prof(prof_id):
    for prof in professores:
        if prof['id'] == prof_id:
            prof['nome'] = data.get('nome', prof['nome']),
            prof['idade'] = data.get('idade', prof['idade']),
            prof['materia'] = data.get('materia', prof['materia']),
            prof['observacoes'] = data.get('observacoes', prof['observacoes'])
            return prof
    raise ProfNaoEncontrado


def delete_prof(prof_id):
    for prof in professores:
        if prof['id'] == prof_id:
            professores.remove(prof)
            return {'mensagem':'professor removido'}
    raise ProfNaoEncontrado




