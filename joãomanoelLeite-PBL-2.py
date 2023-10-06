"""
Sistema operacional:  Windows 11
Versão Python: 3.11.4 64-bit
Autor: João Manoel Naponucena Leite
Componente Curricular: EXA 854 - MI - Algoritimos
Concluído em: 05/10/2023
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""
import os
import random

# Variáveis globais;
pontuacao = 0 # Armazena a pontuação;
contador_jogadas = 0 # Armazena a quantidade de jogadas; 
melhor_pontuacao = 0 # Armazena a melhor pontuação alcançada;
melhor_contador_jogadas = 0 # Armazena o menor número de jogadas para a melhor pontuação;

# Define os termos e tamanho da matriz;
def definirMatriz():
    global pontuacao
    global contador_jogadas

    # Inicializa a matriz de jogo 4x4 com zeros;
    matriz = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    
    # Adiciona dois números aleatórios (2 ou 4) na matriz;
    i, j = random.randint(0, 3), random.randint(0, 3)
    while matriz[i][j] != 0:
        i, j = random.randint(0, 3), random.randint(0, 3)
    matriz[i][j] = random.choice([2, 4])
    
    a, b = random.randint(0, 3), random.randint(0, 3)
    while matriz[a][b] != 0:
        a, b = random.randint(0, 3), random.randint(0, 3)
    matriz[a][b] = random.choice([2, 4])

    # Reiniciar a pontuação e o contador de jogadas;
    pontuacao = 0
    contador_jogadas = 0

    return matriz


# Exibe a matriz;
def exibirMatriz(matriz):
    # Comando para limpar a tela do terminal (funciona no Linux e no Windows);
    os.system('cls' if os.name == 'nt' else 'clear')
    # Exibe a pontuação e a matriz de jogo no terminal;
    print(f"Pontuação: {int(pontuacao/2)} | Jogadas: {contador_jogadas}\n")

    for linha in matriz:
        print("---------------------")
        print("|", end="")
        for numero in linha:
            if numero == 0:
                print("    |", end="")
            else:
                print(f"{numero:3} |", end="")
        print()
    print("---------------------")


# Move os números na matriz;
def mover(tipo_lista):
    nova_lista = [numero for numero in tipo_lista if numero != 0]
    while len(nova_lista) < len(tipo_lista):
        nova_lista.append(0)
    return nova_lista


# Soma os números na matriz;
def somar(tipo_lista):
    pontos = 0
    for i in range(len(tipo_lista) - 1):
        if tipo_lista[i] == tipo_lista[i + 1] and tipo_lista[i] != 0:
            tipo_lista[i] *= 2
            tipo_lista[i + 1] = 0
            pontos += tipo_lista[i]
    return tipo_lista, pontos


# Move e soma os blocos na matriz (junção de duas funções);
def moverSomarBlocos(matriz, direcao):
    global pontuacao
    # Cria uma cópia da matriz;
    matriz_temp = [linha[:] for linha in matriz]
    pontos = 0  # variável local de pontos;

    if direcao == "W":
        for j in range(4):
            coluna = [matriz_temp[i][j] for i in range(4)]
            coluna = mover(coluna)
            coluna, pontos_temp = somar(coluna)
            pontos += pontos_temp  # pontos temporários à pontuação;
            coluna = mover(coluna)
            for i in range(4):
                matriz_temp[i][j] = coluna[i]

    elif direcao == "S":
        for j in range(4):
            coluna = [matriz_temp[i][j] for i in range(4)]
            coluna.reverse()
            coluna = mover(coluna)
            coluna, pontos_temp = somar(coluna)
            pontos += pontos_temp  # pontos temporários à pontuação;
            coluna = mover(coluna)
            coluna.reverse()
            for i in range(4):
                matriz_temp[i][j] = coluna[i]

    elif direcao == "A":
        for i in range(4):
            linha = matriz_temp[i]
            linha = mover(linha)
            linha, pontos_temp = somar(linha)
            pontos += pontos_temp  # pontos temporários à pontuação;
            linha = mover(linha)
            for j in range(4):
                matriz_temp[i][j] = linha[j]

    elif direcao == "D":
        for i in range(4):
            linha = matriz_temp[i]
            linha.reverse()
            linha = mover(linha)
            linha, pontos_temp = somar(linha)
            pontos += pontos_temp  # pontos temporários à pontuação;
            linha = mover(linha)
            linha.reverse()
            for j in range(4):
                matriz_temp[i][j] = linha[j]

    pontuacao += pontos  # soma à pontuação global;
    return matriz_temp


# Adiciona um número (2 ou 4) aleatório na matriz;
def adicionarNumero(matriz):
    i, j = random.randint(0, 3), random.randint(0, 3)
    while matriz[i][j] != 0:
        i, j = random.randint(0, 3), random.randint(0, 3)
    matriz[i][j] = random.choice([2, 4])
    return matriz


# Verifica se ainda existem movimentos válidos;
def verificarJogadas(matriz):
    for direcao in ["W", "S", "A", "D"]:
        if jogadaValida(matriz, direcao):
            return True
    return False


# Verifica se uma jogada é válida em uma determinada direção;
def jogadaValida(matriz, direcao):
    matriz_temp = moverSomarBlocos(matriz, direcao) # Aplica a jogada na matriz temporária;
    return matriz_temp != matriz # Retorna True se a matriz foi alterada após a jogada;


# Verifica se o jogador venceu (alcançou o número 2048);
def verificarFimdeJogo(matriz):
    for linha in matriz:
        for numero in linha:
            if numero == 2048:
                return True
    return False


# Função principal;
def jogo2048():
    global melhor_pontuacao
    global melhor_contador_jogadas
    global contador_jogadas

    flag_1 = 0 
    while flag_1 == 0:
        matriz = definirMatriz()
        exibirMatriz(matriz)
        
        flag_2 = 0
        while flag_2 == 0:
                    
            if verificarFimdeJogo(matriz):
                print('''Você venceu! Parabéns!
Se você conseguiu vencer isso, justamente, você é um verdadeiro nerdola.
⠄⠄⠄⠄⠄⠄⠄⣀⣀⣸⣿⣿⣿⣿⣿⣿⣿⣇⣀⣀⡀⠄⠄⠄⠄⠄⠄ 
⠄⠄⠄⠄⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⠄⠄⠄⠄ 
⠄⠄⢸⣿⣿⡟⠛⠛⠛⢻⣿⣿⣿⣿⣿⣿⣿⡟⠛⠛⠛⢻⣿⣿⡇⠄⠄ 
⠄⠄⠈⠉⠉⠁⠄⠄⠄⠈⠉⠉⣿⣿⣿⠉⠉⠁⠄⠄⠄⠈⠉⠉⠁⠄⠄ 
⣤⣤⡄⠄⣿⣿⣿⠛⠄⠘⠛⠄⣤⣤⣤⠄⠛⠃⠄⠛⢻⣿⣿⠄⢠⣤⣤ 
⣿⣿⡇⠄⠿⢿⣿⣀⠄⠄⠄⠄⣿⣿⣿⠄⠄⠄⠄⣀⣸⡿⠿⠄⢸⣿⣿ 
⣿⣿⣧⣤⠄⠘⠛⠛⠄⠄⠄⣤⣿⣿⣿⣤⠄⠄⠄⠛⠛⠃⠄⣤⣼⣿⣿ 
⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿ 
⠛⢻⣿⣿⣿⣿⣿⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢻⣿⣿⣿⣿⡟⠛ 
⠄⠸⢿⣿⣿⣿⣿⣿⣀⡀⠄⣿⣿⣿⣿⣿⠄⢀⣀⣿⣿⣿⣿⣿⡿⠇⠄ 
⠄⠄⢸⣿⣿⣿⣿⣿⣿⣧⣤⣿⣿⣿⣿⣿⣤⣼⣿⣿⣿⣿⣿⣿⡇⠄⠄ 
⠄⠄⠄⠄⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠄⠄⠄⠄
 ⠄⠄⠄⠄⠄⠄⠄⠉⠉⢹⣿⣿⣿⣿⣿⣿⣿⡏⠉⠉⠁⠄⠄⠄⠄⠄⠄\n''')
                if pontuacao == melhor_pontuacao:
                    if contador_jogadas < melhor_contador_jogadas:
                        melhor_pontuacao = pontuacao
                        melhor_contador_jogadas = contador_jogadas
                if pontuacao > melhor_pontuacao:
                    melhor_pontuacao = pontuacao
                    melhor_contador_jogadas = contador_jogadas
                    print(f"É um novo recorde! de {int(melhor_pontuacao/2)} pontos com {contador_jogadas} jogadas!")
                    flag_2 += 1
                else:
                    print(f"É um novo recorde! de {int(melhor_pontuacao/2)} pontos com {contador_jogadas} jogadas!")
                    flag_2 += 1

            elif not verificarJogadas(matriz):
                print('''Fim de jogo! Você perdeu
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼''')
                if pontuacao == melhor_pontuacao:
                    if contador_jogadas < melhor_contador_jogadas:
                        melhor_pontuacao = pontuacao
                        melhor_contador_jogadas = contador_jogadas
                if pontuacao > melhor_pontuacao:
                    melhor_pontuacao = pontuacao
                    melhor_contador_jogadas = contador_jogadas
                    print(f"É um novo recorde! de {int(melhor_pontuacao/2)} pontos com {contador_jogadas} jogadas!")
                    flag_2 += 1
                else:
                    print(f"É um novo recorde! de {int(melhor_pontuacao/2)} pontos com {contador_jogadas} jogadas!")
                    flag_2 += 1

            if flag_2 == 0:
                direcao = input("Digite uma direção (W/A/S/D): ").upper()
                if direcao not in ["W", "A", "S", "D"]:
                    print("Direção inválida. Use W, A, S ou D.")
                    continue

                matriz_temp = moverSomarBlocos(matriz, direcao)
                if matriz_temp == matriz:
                    print("Movimento sem sentido! Tente novamente.")
                    continue

                contador_jogadas += 1     
                matriz = matriz_temp
                matriz = adicionarNumero(matriz)
                exibirMatriz(matriz)

        flag_3 = 0
        while flag_3 == 0:
            confirmar = input("Deseja jogar novamente(S/N)?").upper()
            if confirmar in ("S", "N"):
                if confirmar == "S":
                    flag_1 == 0
                    flag_3 += 1
                if confirmar == "N":
                    flag_1 += 1
                    flag_3 += 1
            else:
                print("Entrada inválida! Tente novamente")  

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Maior pontuação atual: {int(melhor_pontuacao/2)} pontos | jogadas: {melhor_contador_jogadas}")
    print('''Obrigado por jogar!
░░░░░░░░░░░░░░░░░░░░░░█████████
░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███
░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███
░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███
░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
░░████████████░░░█████████████████''')


if __name__ == "__main__":
    jogo2048()
