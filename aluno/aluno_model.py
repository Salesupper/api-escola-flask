from dados import alunos


class AlunoNaoEncontrado(Exception):
    pass


def media(n1,n2):
    return (n1+n2)/2


def get_alunos():
    for aluno in alunos:
        if aluno['media'] == None:
            aluno['media'] = media(aluno['nota_b1'], aluno['nota_b2'])
    return(alunos)


def get_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            return aluno
    raise AlunoNaoEncontrado


def create_aluno():
    data = {
        'id': len(alunos) + 1,
        'nome': aluno['nome'],
        'idade': aluno['idade'],
        'turma': aluno['turma'],
        'nascimento': aluno['nascimento'],
        'nota_b1': aluno['nota_b1'],
        'nota_b2': aluno['nota_b2'],
        'media': media(aluno['nota_b1'],aluno['nota_b2'])
    }
    alunos.append(data)
    

def update_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            aluno['nome'] = data.get('nome', aluno['nome']),
            aluno['idade'] = data.get('idade', aluno['idade']),
            aluno['turma'] = data.get('turma', aluno['turma']),
            aluno['nascimento'] = data.get('nascimento', aluno['nascimento'])
            aluno['nota_b1'] = data.get('nota_b1', aluno['nota_b1']),
            aluno['nota_b2'] = data.get('nota_b2', aluno['nota_b2']),
            aluno['media'] = data.get('media', aluno['media'])
            return aluno
    raise AlunoNaoEncontrado


def delete_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            alunos.remove(aluno)
            return {'mensagem':'aluno removido'}
    raise AlunoNaoEncontrado



