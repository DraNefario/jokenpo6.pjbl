import random

opcoes = ["pedra", "papel", "tesoura"]
vezesJogadas = 0
placarJogador = 0 
placarComputador = 0
placarJogador1 = 0
placarJogador2 = 0
placarComputador1 = 0
placarComputador2 = 0

while True:
    print("foram jogadas",vezesJogadas, "partidas")
    print("pontos do jogador = ",placarJogador)
    print("pontos da maquina = ",placarComputador)
    print("pontos do jogador 1 = ",placarJogador1)
    print("pontos da jogador 2 = ",placarJogador2)
    print("pontos do computador 1 = ",placarComputador1)
    print("pontos do computador 2 = ",placarComputador2)

    modo = input("Digite 1 para humano vs máquina, 2 para humano vs humano e 3 para máquina vs máquina (ou 'sair' para encerrar): ")

    if modo == 'sair':
        print("Obrigado por jogar!")
        break

    modo = int(modo)

    if modo == 1:
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
            vezesJogadas += 1
        elif (jogador == "pedra" and computador == "tesoura") or \
                (jogador == "papel" and computador == "pedra") or \
                (jogador == "tesoura" and computador == "papel"):
            print("Você ganhou!")
            vezesJogadas += 1
            placarJogador +=1
        else:
            print("Você perdeu!")
            vezesJogadas += 1
            placarComputador +=1

    elif modo == 2:
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
            vezesJogadas += 1
        elif (jogador1 == "pedra" and jogador2 == "tesoura") or \
                (jogador1 == "papel" and jogador2 == "pedra") or \
                (jogador1 == "tesoura" and jogador2 == "papel"):
            print("O jogador 1 ganhou!")
            vezesJogadas += 1
            placarJogador1 +=1
        else:
            print("O jogador 2 ganhou!")
            vezesJogadas += 1
            placarJogador2 +=1

    elif modo == 3:
        computador1 = random.choice(opcoes)
        print("A escolha do computador foi", computador1)

        computador2 = random.choice(opcoes)
        print("A escolha do computador foi", computador2)

        if computador1 == computador2:
            print("Empate!")
            vezesJogadas += 1
        elif (computador1 == "pedra" and computador2 == "tesoura") or \
                (computador1 == "papel" and computador2 == "pedra") or \
                (computador1 == "tesoura" and computador2 == "papel"):
            print("O computador 1 ganhou!")
            vezesJogadas += 1
            placarComputador1 +=1
        else:
            print("O computador 2 ganhou!")
            vezesJogadas += 1
            placarComputador2 +=1
