import random

acoes_possiveis = ["pedra", "papel", "tesoura"]
acao_Bot0 = random.choice(acoes_possiveis)
acao_Bot1 = random.choice(acoes_possiveis)
print(f"O computador 1 escolheu {acao_Bot0}, o computador 2 escolheu {acao_Bot1}.")

if acao_Bot0 == acao_Bot1:
    print(f"O jogo empatou, ambos os computadores escolheram a mesma opcao.")
elif acao_Bot0 == "pedra":
    if acao_Bot1 == "tesoura":
        print("Pedra ganha de tesoura, o computador 1 venceu.")
    else:
        print ("Papel ganha de pedra, o computador 2 venceu.")
elif acao_Bot0 == "papel":
    if acao_Bot1 == "pedra":
        print("Papel ganha de pedra, o computador 1 venceu.")
    else:
        print("Tesoura ganha de papel, o computador 2 venceu.")
elif acao_Bot0 == "tesoura":
    if acao_Bot1 == "papel":
        print("Tesoura ganha de papel, o computador 1 venceu.")
    else:
        print("Pedra ganha de tesoura, o computador 2 venceu.")