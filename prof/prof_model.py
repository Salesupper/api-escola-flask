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


def create_prof(data):
    prof = {
        'id': len(professores) + 1,
        'nome': data['nome'],
        'idade': data['idade'],
        'materia': data['materia'],
        'observacoes': data['observacoes']
    }
    professores.append(prof)


def update_prof(prof_id, data):
    prof = get_prof(prof_id)
    p = {
        'id': prof_id,
        'nome': data['nome'],
        'idade': data['idade'],
        'materia': data['materia'],
        'observacoes': data['observacoes']
    }
    prof.update(p)


def delete_prof(prof_id):
    prof = get_prof(prof_id)
    professores.remove(prof)
    return {'mensagem':'professor removido'}





