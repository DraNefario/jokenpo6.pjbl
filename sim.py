import random

pedra = "pedra"
papel = "papel"
tesoura = "tesoura"

vezesJogadas = 0
placarJogador = 0 
placarComputador = 0
placarJogador1 = 0
placarJogador2 = 0
placarComputador1 = 0
placarComputador2 = 0

modo = input("Digite 1 para humano vs máquina, 2 para humano vs humano e 3 para máquina vs máquina (ou 'sair' para encerrar): ")

while modo != 'sair':
    modo = int(modo)
    if modo == 1:
        continuar_jogando = True
        while continuar_jogando:
            jogador = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()
            if jogador == "sair":
                print("foram jogadas", vezesJogadas, "partidas")
                print("pontos do jogador = ", placarJogador)
                print("pontos da máquina = ", placarComputador)
                print("Obrigado por jogar!")
                print("Alunos: Danillo, Ricardo, Samuel, Thomas")
                continuar_jogando = False
                break
            elif jogador != pedra and jogador != papel and jogador != tesoura:
                print("Escolha inválida. Por favor, digite uma escolha válida.")
                continue

            num_aleatorio = random.randint(0, 2)
            if num_aleatorio == 0:
                computador = pedra
            elif num_aleatorio == 1:
                computador = papel
            else:
                computador = tesoura

            print("A escolha do computador foi", computador)

            if computador == jogador:
                print("Empate!")
                print("pontos do jogador = ", placarJogador)
                print("pontos da máquina = ", placarComputador)
                vezesJogadas += 1
            elif (jogador == pedra and computador == tesoura) or \
                    (jogador == papel and computador == pedra) or \
                    (jogador == tesoura and computador == papel):
                print("Você ganhou!")
                print("pontos do jogador = ", placarJogador)
                print("pontos da máquina = ", placarComputador)
                vezesJogadas += 1
                placarJogador +=1
            else:
                print("Você perdeu!")
                vezesJogadas += 1
                placarComputador +=1
                print("pontos do jogador = ", placarJogador)
                print("pontos da máquina = ", placarComputador)

            continuar = input("Digite 'continuar' para jogar novamente ou 'sair' para encerrar: ")
            if continuar.lower() == 'sair':
                print("foram jogadas", vezesJogadas, "partidas")
                print("pontos do jogador = ", placarJogador)
                print("pontos da máquina = ", placarComputador)
                print("Obrigado por jogar!")
                print("Alunos: Danillo, Ricardo, Samuel, Thomas")
                continuar_jogando = False
                break

    elif modo == 2:
        continuar_jogando = True
        while continuar_jogando:
            jogador1 = input("Jogador 1, escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()
            if jogador1 == "sair":
                print("foram jogadas", vezesJogadas, "partidas")
                print("pontos do jogador 1 = ", placarJogador1)
                print("pontos do jogador 2 = ", placarJogador2)
                print("Obrigado por jogar!")
                print("Alunos: Danillo, Ricardo, Samuel, Thomas")
                continuar_jogando = False
                break
            elif jogador1 != pedra and jogador1 != papel and jogador1 != tesoura:
                print("Escolha inválida. Por favor, digite uma escolha válida.")
                continue
            
            jogador2 = input("Jogador 2, escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()
            if jogador2 == "sair":
                print("foram jogadas", vezesJogadas, "partidas")
                print("pontos do jogador 1 = ", placarJogador1)
                print("pontos do jogador 2 = ", placarJogador2)
                print("Obrigado por jogar!")
                print("Alunos: Danillo, Ricardo, Samuel, Thomas")
                continuar_jogando = False
                break
            elif jogador2 != pedra and jogador2 != papel and jogador2 != tesoura:
                print("Escolha inválida. Por favor, digite uma escolha válida.")
                continue
            
            print("A escolha do jogador 1 foi", jogador1, "e a escolha do jogador 2 foi", jogador2)
            
            if jogador1 == jogador2:
                print("Empate!")
                print("pontos do jogador = ", placarJogador1)
                print("pontos da máquina = ", placarJogador2)
                vezesJogadas += 1
            elif (jogador1 == pedra and jogador2 == tesoura) or \
                    (jogador1 == papel and jogador2 == pedra) or \
                    (jogador1 == tesoura and jogador2 == papel):
                print("O jogador 1 ganhou!")
                print("pontos do jogador = ", placarJogador1)
                print("pontos da máquina = ", placarJogador2)
                vezesJogadas += 1
                placarJogador1 +=1
            else:
                print("O jogador 2 ganhou!")
                print("pontos do jogador = ", placarJogador1)
                print("pontos da máquina = ", placarJogador2)
                vezesJogadas += 1
                placarJogador2 +=1

            continuar = input("Digite 'continuar' para jogar novamente ou 'sair' para encerrar: ")
            if continuar.lower() == 'sair':
                print("foram jogadas", vezesJogadas, "partidas")
                print("pontos do jogador = ", placarJogador1)
                print("pontos da máquina = ", placarJogador2)
                print("Obrigado por jogar!")
                print("Alunos: Danillo, Ricardo, Samuel, Thomas")
                continuar_jogando = False
                break
                
    elif modo == 3:
          continuar_jogando = True
          while continuar_jogando:
            num_aleatorio1 = random.randint(0, 2)
            if num_aleatorio1 == 0:
                computador1 = pedra
            elif num_aleatorio1 == 1:
                computador1 = papel
            else:
                computador1 = tesoura

            num_aleatorio2 = random.randint(0, 2)
            if num_aleatorio2 == 0:
                computador2 = pedra
            elif num_aleatorio2 == 1:
                computador2 = papel
            else:
                computador2 = tesoura

            print("A escolha do computador 1 foi", computador1)
            print("A escolha do computador 2 foi", computador2)

            if computador1 == computador2:
                print("Empate!")
                print("pontos do jogador = ", placarComputador1)
                print("pontos da máquina = ", placarComputador2)
                vezesJogadas += 1
            elif (computador1 == pedra and computador2 == tesoura) or \
                    (computador1 == papel and computador2 == pedra) or \
                    (computador1 == tesoura and computador2 == papel):
                print("O computador 1 ganhou!")
                print("pontos do jogador = ", placarComputador1)
                print("pontos da máquina = ", placarComputador2)
                placarComputador1 += 1
                vezesJogadas += 1
            else:
                print("O computador 2 ganhou!")
                print("pontos do jogador = ", placarComputador1)
                print("pontos da máquina = ", placarComputador)
                placarComputador2 += 1
                vezesJogadas += 1


            continuar = input("Digite 'continuar' para jogar novamente ou 'sair' para encerrar: ")
            if continuar.lower() == 'sair':
                print("foram jogadas", vezesJogadas, "partidas")
                print("pontos do jogador 1 = ", placarComputador1)
                print("pontos do jogador 2 = ", placarComputador2)
                print("Obrigado por jogar!")
                print("Alunos: Danillo, Ricardo, Samuel, Thomas")
                continuar_jogando = False
                break  

    break   