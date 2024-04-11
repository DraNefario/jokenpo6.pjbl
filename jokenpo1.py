import random

opcoes = ["pedra", "papel", "tesoura"]

while True:
    jogador = input("escolha pedra, papel ou tesoura(ou 'sair' para encerrar): ".lower())
    if jogador == "sair":
      print("obrigado por jogar!")
      break
    elif jogador not in ["pedra", "papel", "tesoura"]:
       print("escolha invalida. Por favor digte uma escolha valida")
       continue

    computador = random.choices(opcoes)
    print("a escolha do computador foi", str(computador))

    if computador == jogador:
       print("empate!")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        print("Você ganhou!")
    else: 
       print("voce perdeu!")