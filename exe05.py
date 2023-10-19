print(f'{"Análise de Jogadores":=^50}')
while True:
    try:
        n = int(input('Digite o número de Jogadores para análise: '))
        if n > 0:
            break
        else:
            print(f'Erro -> O valor deve ser maior do que zero! ', end='')
    except Exception as e:
        print(f'Exceção -> {e}')

jogador = {}
listaJogadores = []
listaGol = []
for i in range(n):
    jogador['nome'] = str(input(f'Nome {i+1}º Jogador: ')).title().strip()
    while True:
        try:
            partidas = int(input(f'Número de partidas que {jogador["nome"]} jogou: '))
            if partidas >= 1:
                break
            else:
                print(f'Erro: O número de partidas não pode ser zero ou negativo!')
        except Exception as e:
            print(f'Exceção -> {e}')
    for j in range(partidas):
        while True:
            try:
                gol = int(input(f'  Número de gols da {j + 1}° partida: '))
                if gol >= 0:
                    listaGol.append(gol)
                    break
                else:
                    print(f'Erro -> O númere de gols não pode ser negativo! ')
            except Exception as e:
                print(f'Exceção: {e}')
    jogador['gols'] = listaGol[:]
    jogador['totalGols'] = sum(listaGol)
    listaJogadores.append(jogador.copy())
    listaGol.clear()

print(f'{"Menu de Jogadores":=^80}')
print(f'{"Código":<10}|{"Jogador":<20}|{"Total Gols":<15}|{"Gols":<40}')
for i, d in enumerate(listaJogadores):
    print(f'{i+1:<10}|{d["nome"]:<20}|{d["totalGols"]:<15}|{d["gols"]}{"":<40}', end='')
    print()

while True:
    while True:
        try:
            codigo = int(input("Digite o código do jogador: "))
            if 1 <= codigo <= len(listaJogadores):
                break
            else:
                print(f'Erro -> Digite um código entre 1 e {len(listaJogadores)}')
        except Exception as e:
            print(f'Exceção -> {e}')

    print(f'Jogador: {listaJogadores[codigo-1]["nome"]}, jogou {len(listaJogadores[codigo-1]["gols"])} partidas!')
    for i, v in enumerate(listaJogadores[codigo-1]["gols"]):
        print(f'Na {i + 1}° partida fez: {v} gols')

    while True:
        resp = str(input('Deseja consultar um novo jogador: (s)im | (n)ao: ')).lower().strip()
        if resp in 'sn':
            break
        else:
            print(f'Erro: Você deve digitar s ou N. ', end='')

    if resp == 'n':
        break
print(f'Fim do programa!')