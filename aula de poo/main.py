from Classe import *
def menu():
    p = Pessoa()
    continuar = True
    while continuar:
        print("\nEscolha uma ação:")
        print("1. Falar")
        print("2. Comer")
        print("3. Dormir")
        print("4. Sair")

        escolha = input("Digite o número da ação desejada: ")

        if escolha == '1':
            p.falar()
        elif escolha == '2':
            p.comer()
        elif escolha == '3':
            p.dormir()
        elif escolha == '4':
            print("Saindo do programa...")
            continuar = False
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
