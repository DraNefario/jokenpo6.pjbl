import random

opcoes = ["pedra", "papel", "tesoura"]

while True:
    modo = input("Digite 1 para humano vs humano, 2 para humano vs máquina e 3 para máquina vs máquina (ou 'sair' para encerrar): ")

    if modo == 'sair':
        print("Obrigado por jogar!")
        break

    modo = int(modo)

    if modo == 2:
        jogador = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()
        if jogador == "sair":
            print("Obrigado por jogar!")
            break
        elif jogador not in ["pedra", "papel", "tesoura"]:
            print("Escolha inválida. Por favor, digite uma escolha válida.")
            continue

        computador = random.choice(opcoes)
        print("A escolha do computador foi", computador)

        if computador == jogador:
            print("Empate!")
        elif (jogador == "pedra" and computador == "tesoura") or \
                (jogador == "papel" and computador == "pedra") or \
                (jogador == "tesoura" and computador == "papel"):
            print("Você ganhou!")
        else:
            print("Você perdeu!")

    elif modo == 1:
        jogador1 = input("Jogador 1, escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()
        if jogador1 == "sair":
            print("Obrigado por jogar!")
            break
        elif jogador1 not in ["pedra", "papel", "tesoura"]:
            print("Escolha inválida. Por favor, digite uma escolha válida.")
            continue
        
        jogador2 = input("Jogador 2, escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()
        if jogador2 == "sair":
            print("Obrigado por jogar!")
            break
        elif jogador2 not in ["pedra", "papel", "tesoura"]:
            print("Escolha inválida. Por favor, digite uma escolha válida.")
            continue
        
        print("A escolha do jogador 1 foi", jogador1, "e a escolha do jogador 2 foi", jogador2)
        
        if jogador1 == jogador2:
            print("Empate!")
        elif (jogador1 == "pedra" and jogador2 == "tesoura") or \
                (jogador1 == "papel" and jogador2 == "pedra") or \
                (jogador1 == "tesoura" and jogador2 == "papel"):
            print("O jogador 1 ganhou!")
        else:
            print("O jogador 2 ganhou!")

    elif modo == 3:
        computador1 = random.choice(opcoes)
        print("A escolha do computador foi", computador1)

        computador2 = random.choice(opcoes)
        print("A escolha do computador foi", computador2)

        if computador1 == computador2:
            print("Empate!")
        elif (computador1 == "pedra" and computador2 == "tesoura") or \
                (computador1 == "papel" and computador2 == "pedra") or \
                (computador1 == "tesoura" and computador2 == "papel"):
            print("O computador 1 ganhou!")
        else:
            print("O computador 2 ganhou!")