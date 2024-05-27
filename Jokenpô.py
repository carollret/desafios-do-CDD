from random import randint
perg = 'S'
while perg.upper() == "S":
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(1, 3)
    print('Suas opções: \n'
          '[1] PEDRA\n'
          '[2] PAPEL\n'
          '[3] TESOURA\n')

    jogador = int(input('Qual é a sua jogada? '))

    if jogador not in [1, 2, 3]:
        print('JOGADA INVÁLIDA!')
    else:
        print('_=' * 12)
        print('Computador jogou {}'.format(itens[computador - 1]))
        print('Jogador jogou {}'.format(itens[jogador - 1]))
        print('_=' * 12)

        if computador == 1:  # Pedra
            if jogador == 1:
                print('EMPATE')
            elif jogador == 2:
                print('JOGADOR VENCE')
            elif jogador == 3:
                print('COMPUTADOR VENCE')
        elif computador == 2:  # Papel
            if jogador == 1:
                print('COMPUTADOR VENCE')
            elif jogador == 2:
                print('EMPATE')
            elif jogador == 3:
                print('JOGADOR VENCE')
        elif computador == 3:  # Tesoura
            if jogador == 1:
                print('JOGADOR VENCE')
            elif jogador == 2:
                print('COMPUTADOR VENCE')
            elif jogador == 3:
                print('EMPATE')
        print('_=' * 12)
    perg = input("Quer jogar novamente? (S/N) ").strip().upper()

    if perg != "S": #Parar loop se a resposta foi 'n'
        break
