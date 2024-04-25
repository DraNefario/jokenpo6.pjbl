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
#Escolhe o modo de jogo antes do loop, ou seja não pode mudar de modo após a seleçao, somente quando reiniciar.
modo = input("Bem-vindo! Pressione 1 para Humano vs. Computador, 2 para Humano vs. Humano, 3 para Computador vs. Computador e 'sair' para finalizar para finalizar o Jokenpô:")
#Inicia o loop dos modos que para quando o modo for igual a sair.
while modo != 'sair':
    modo = int(modo)
    if modo == 1:
        #Variável para verificar se o jogador continuará ou irá sair, enquanto true o jogo continua.
        continuar_jogando = True
        while continuar_jogando:
            jogador = input("Digite pedra, papel ou tesoura :").lower()
           
            #Verificar se o que ele escreveu está de acordo com as opções de jogo
            if jogador != pedra and jogador != papel and jogador != tesoura:
                print("Escolha inválida. Por favor, digite uma escolha válida.")
                continue
            #Escolhe um número aleatório entre 0 e 2 com uma respectiva escolha para cada número.
            num_aleatorio = random.randint(0, 2)
            if num_aleatorio == 0:
                computador = pedra
            elif num_aleatorio == 1:
                computador = papel
            else:
                computador = tesoura

            print("A escolha do computador foi", computador)
            #Se a escolha do computador for a mesma do jogador printa empate e mostra o placar.
            if computador == jogador:
                print("Empate!")
                vezesJogadas += 1
                print("Pontuação do jogador = ", placarJogador)
                print("Pontuação do computador = ", placarComputador)
                #Caso isso não ocorra temos duas opções o jogador vencer ou perder.
            elif (jogador == pedra and computador == tesoura) or \
                    (jogador == papel and computador == pedra) or \
                    (jogador == tesoura and computador == papel):
                print("Você ganhou")
                vezesJogadas += 1
                placarJogador +=1
                print("Pontuação do jogador = ", placarJogador)
                print("Pontuação do computador = ", placarComputador)
            else:
                print("Você perdeu")
                vezesJogadas += 1
                placarComputador +=1
                print("Pontuação do jogador = ", placarJogador)
                print("Pontuação do computador = ", placarComputador)
              #Aqui, ao final da partida, temos a opção de continuar jogando ou sair.
            continuar = input("Digitar 'continuar' para jogar de novo ou 'sair' para finalizá-lo:")
            if continuar.lower() == 'sair':
                print("foram jogadas", vezesJogadas, "partidas")
                print("Pontuação do jogador = ", placarJogador)
                print("Pontuação do computador = ", placarComputador)
                print("Obrigado por jogar o nosso Jokenpô!!")
                print("Alunos: Danillo, Rodrigo, Samuel, Thomas")
                continuar_jogando = False
                break

    elif modo == 2:
        continuar_jogando = True
        while continuar_jogando:
            #Jogador 1 escolhe o objeto de jogo.
            jogador1 = input("Jogador 1, digite pedra, papel ou tesoura : ").lower()
            #Verifica se ele escolheu um objeto dentro dos parâmetros do código.
            if jogador1 != tesoura and jogador1 != papel and jogador1 != pedra:
                print("Escolha inválida. Por favor, digite uma escolha válida.")
                continue
            #Jogador 2 escolhe o objeto.
            jogador2 = input("Jogador 2, digite pedra, papel ou tesoura : ").lower()
            #Verifica se jogador 2 escolheu algo nos parâmetros do código.
            if jogador2 != tesoura and jogador2 != papel and jogador2 != pedra:
                print("Escolha inválida. Por favor, digite uma escolha válida.")
                continue
            
            print("Resultado: as jogadas dos jogadores 1 e 2 foram de:", jogador1,"e", jogador2,",respectivamente.")
            #Caso jogador 1 e 2 tenham escolhido o mesmo objeto empate.
            if jogador1 == jogador2:
                print("Empate")
                print("Pontuação do jogador_1 = ", placarJogador1)
                print("Pontuação do jogador_2 = ", placarJogador2)
                vezesJogadas += 1
                #Caso não ocorra empate temos as condiçoes de vitória do jogador 1.
            elif (jogador1 == pedra and jogador2 == tesoura) or \
                    (jogador1 == papel and jogador2 == pedra) or \
                    (jogador1 == tesoura and jogador2 == papel):
                print("O jogador_1 ganhou!")
                vezesJogadas += 1
                placarJogador1 +=1
                print("Pontuação do jogador_1 = ", placarJogador1)
                print("Pontuação do jogador_2 = ", placarJogador2)
                #Se nenhum do anteriores ocorrer então o jogador 1 perdeu.
            else:
                print("O jogador_2 ganhou!")
                vezesJogadas += 1
                placarJogador2 +=1
                print("Pontuação do jogador_1 = ", placarJogador1)
                print("Pontuação do jogador_2 = ", placarJogador2)
                #Opção de continuar jogando ou sair caso sair mostra a tabela. 
            continuar = input("Digite continuar para jogar novamente ou sair para encerrar: ")
            if continuar.lower() == 'sair':
                print("foram jogadas", vezesJogadas, "partidas")
                print("Pontuação do jogador_1 = ", placarJogador1)
                print("Pontuação do jogador_2 = ", placarJogador2)
                print("Obrigado por jogar o nosso Jokenpô!!")
                print("Alunos: Danillo, Rodrigo, Samuel, Thomas")
                continuar_jogando = False
                break
                
    #Introduz o modo 3 (Computador vs. Computador) caso o jogador queira continuar jogando. 
    #Utilização da biblioteca Random para escolher de forma aleatória entre pedra papel e tesoura para Computadores 1 e 2.         
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

            #Printa a escolha do computador 1 e 2.
            print("A escolha do computador_1 foi", computador1)
            print("A escolha do computador_2 foi", computador2)
            
            #Se computador 1 escolher a mesma coisa que o computador 2, empate.
            if computador1 == computador2:
                print("Empate!")
                print("Pontuação do computador_1 = ", placarComputador1)
                print("Pontuação da computador_2 = ", placarComputador2)
                vezesJogadas += 1
                
            #Se computador 1 escolher pedra e computador 2 escolher tesoura ou
            #Computador 1 escolher papel e computador 2 escolher pedra ou
            #Computador 2 escolher tesoura e computador 2 escolher papel
            #Computador 1 ganha.
            elif (computador1 == pedra and computador2 == tesoura) or \
                    (computador1 == papel and computador2 == pedra) or \
                    (computador1 == tesoura and computador2 == papel):
                print("O computador 1 ganhou!")
                placarComputador1 += 1
                vezesJogadas += 1
                print("Pontuação do computador_1 = ", placarComputador1)
                print("Pontuação do computador_2 = ", placarComputador2)

            #Caso contrário, o computador 2 ganha.
            else:
                print("O computador_2 ganhou!")
                placarComputador2 += 1
                vezesJogadas += 1
                print("Pontuação do computador_1 = ", placarComputador1)
                print("Pontuação do computador_2 = ", placarComputador2)

            #Oferece ao usuário a opção de continuar jogando ou para sair do programa.
            #Caso deseje finalizar, mostra a quantidade de partidas jogadas e a pontuação do computador 1 e 2
            #Mostra também os agradecimentos e os nomes dos alunos e finaliza o programa.
            #Caso deseje continuar, o programa continua o modo.
            continuar = input("Digite continuar para jogar o Jokenpô de novo ou sair para finalizar o Jokenpô: ")
            if continuar.lower() == 'sair':
                print("foram jogadas", vezesJogadas, "partidas")
                print("Pontuação do computador_1 = ", placarComputador1)
                print("Pontuação do computador_2 = ", placarComputador2)
                print("Obrigado por jogar o nosso Jokenpô!!")
                print("Alunos: Danillo, Rodrigo, Samuel, Thomas")
                continuar_jogando = False
                break

    break
