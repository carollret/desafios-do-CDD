def exibirTabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)
def verificarVitoria(tabuleiro, jogador):
    for linha in tabuleiro:     # Verifica linhas
        if all(c == jogador for c in linha):
            return True
    for coluna in range(3):     # Verifica colunas
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):     # Verifica diagonais
        return True
    return False
def jogoDaVelha():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogadorAtual = 'X'
    jogadas = 0

    while True:
        exibirTabuleiro(tabuleiro)
        try:
            linha = int(input(f'Jogador {jogadorAtual}, escolha a linha (1, 2 ou 3): ')) - 1
            coluna = int(input(f'Jogador {jogadorAtual}, escolha a coluna (1, 2 ou 3): ')) - 1
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if 0 <= linha <= 2 and 0 <= coluna <= 2:
            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = jogadorAtual
                jogadas += 1
            else:
                print("Essa posição já está ocupada. Tente novamente.")
                continue
        else:
            print("Posição inválida. Tente novamente.")
            continue

        if verificarVitoria(tabuleiro, jogadorAtual):
            exibirTabuleiro(tabuleiro)
            print(f'Jogador {jogadorAtual} venceu!')
            break
        elif jogadas == 9:
            exibirTabuleiro(tabuleiro)
            print('O jogo é um empate!')
            break
        else:
            jogadorAtual = 'O' if jogadorAtual == 'X' else 'X'

if __name__ == "__main__":
    jogoDaVelha()
