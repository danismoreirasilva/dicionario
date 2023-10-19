aluno = {}
print(f'{"Dados do aluno":=^40}')

aluno['nome'] = str(input('Nome: ')).title().strip()
aluno['media'] = float(input('Média: '))

if aluno['media'] >= 6:
    aluno['status'] = 'aprovado'
else:
    aluno['status'] = 'reprovado'

print(f'{"Boletim - Acesso Direto":=^40}')
print(f'Nome: {aluno["nome"]}')
print(f'Média: {aluno["media"]}')
print(f'Situação: {aluno["status"].title()}')

print()

#Abaixo é um exemplo de laço de repetição para dicionários
#como temos apenas 1 registro, não seria necessário implementar o for.
#Fica de exemplo para vocês a sintaxe!
print(f'{"Boletim - Acesso Laço(For)":=^40}')
for k, v in aluno.items():
    print(f'{k}: {v}')
