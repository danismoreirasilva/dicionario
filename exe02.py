from datetime import datetime

print(f'{"Digite os dados do Trabalhador":=^40}')
trabalhador = {}

trabalhador['nome'] = str(input('Nome: ')).title().strip()
trabalhador['anoNasc'] = int(input('Ano Nascimento: '))
trabalhador['idade'] = datetime.now().year - trabalhador['anoNasc']
trabalhador['ctps'] = int(input('Nº CTPS: '))
if trabalhador['ctps'] != 0:
    trabalhador['anoContrato'] = int(input('Ano Contratação: '))
    trabalhador['salario'] = float(input('Salário: R$ '))
    trabalhador['aposentar'] = trabalhador['idade'] + 35 - (datetime.now().year - trabalhador["anoContrato"])

print(f'{"Sobre o Trabalhador":=^40}')
if trabalhador['ctps'] != 0:
    for k, v in trabalhador.items():
        print(f'{k}: {v}')
    print(f'Faltam {35 - (datetime.now().year - trabalhador["anoContrato"])} anos para se aposentar!')

else:
    for k, v in trabalhador.items():
        print(f'{k}: {v}')
