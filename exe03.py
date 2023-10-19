jogador = {}
listaGols = []
jogador['nome'] = str(input('Nome Jogador: '))
jogador['partidas'] = int(input('Quantidade partidas: '))

for i in range(jogador['partidas']):
    qteGols = int(input(f'***Nº de gols da {i+1}° partida: '))
    listaGols.append(qteGols)

jogador['gols'] = listaGols[:]
jogador['totalGols'] = sum(listaGols)

print(f'{"Visualizando o dicionário":=^40}')
for k, v in jogador.items():
    print(f'Chave {k} tem valor: {v}')

print(f'{"Sobre o Jogador":=^40}')
print(f'O jogador {jogador["nome"].title()} esteve em {jogador["partidas"]} partidas')

for i, v in enumerate(jogador['gols']):
    print(f'Na {i+1}° partida fez: {v} gol(s)')
print(f'{jogador["nome"].title()} fez {jogador["totalGols"]} gols!')