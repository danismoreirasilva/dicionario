pessoa = {}
listaPessoas = []
listaMulheres = []
somaIdade = media = 0
while True:
    while True:
        nome = str(input('Nome: ')).title().strip()
        if nome.isspace() or len(nome) == 0:
            print(f'Erro -> O nome da pessoa não pode ser vazio! ', end='')
        else:
            pessoa['nome'] = nome
            break
    while True:
        sexo = str(input('Sexo biológico: (f)eminino | (m)asculino: ')).lower().strip()
        if sexo in 'fm':
            pessoa['sexo'] = sexo
            break
        else:
            print(f'Erro -> Digite "f" ou "m"! ', end='')

    while True:
        try:
            idade = int(input('Idade: '))
            if 1 <= idade <= 120:
                pessoa['idade'] = idade
                break
            else:
                print(f'Erro -> Idade inváliado, o valor deve estar entre 1 e 120!')
        except Exception as e:
            print(f'Exceção -> {e}')

    listaPessoas.append(pessoa.copy())
    pessoa.clear()

    while True:
        resp = str(input('Deseja cadastrar uma nova pessoa: (s)im | (n)ao: ')).lower().strip()
        if resp in 'sn':
            break
        else:
            print(f'Erro: Você deve digitar s ou N. ', end='')

    if resp == 'n':
        break

print(f'{"Análise dos Dados":=^40}')
print(f'Formam cadastradas: {len(listaPessoas)} pessoas')

for d in listaPessoas:
    somaIdade += d['idade']

media = somaIdade / len(listaPessoas)
print(f'A média de idades é: {media:5.2f} anos.')

for d in listaPessoas:
    if d['sexo'] == 'f':
        listaMulheres.append(d['nome'])

if len(listaMulheres) > 0:
    print(f'A lista de mulheres é: {listaMulheres}')
else:
    print(f'Não foi cadastrado nenhuma pessoa do sexo Feminino!')

print(f'Relação de pessoas acima da média de idade')

for d in listaPessoas:
    if d['idade'] >= media:
        for k, v in d.items():
            print(f'{k}: {v} | ', end='')
        print()


print(f'Fim do programa!')
