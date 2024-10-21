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


def create_aluno(data):
    aluno = {
        'id': len(alunos) + 1,
        'nome': data['nome'],
        'idade': data['idade'],
        'turma': data['turma'],
        'nascimento': data['nascimento'],
        'nota_b1': data['nota_b1'],
        'nota_b2': data['nota_b2'],
        'media': media(data['nota_b1'],data['nota_b2'])
    }
    alunos.append(aluno)
    

def update_aluno(aluno_id, data):
    aluno = get_aluno(aluno_id)
    a = {
        'id': aluno_id,
        'nome': data['nome'],
        'idade': data['idade'],
        'turma': data['turma'],
        'nascimento': data['nascimento'],
        'nota_b1': data['nota_b1'],
        'nota_b2': data['nota_b2'],
        'media': media(data['nota_b1'],data['nota_b2'])
    }
    aluno.update(a)

   
def delete_aluno(aluno_id):
    aluno = get_aluno(aluno_id)
    alunos.remove(aluno)
    return {'mensagem':'aluno removido'}




