import random

acao_Humana = input("Escolha sua jogada (pedra, papel ou tesoura): ")

acoes_possiveis = ["pedra", "papel", "tesoura"]
acao_Bot = random.choice(acoes_possiveis)
print(f"Voce escolheu {acao_Humana}, o computador escolheu {acao_Bot}.")

if acao_Humana == acao_Bot:
    print(f"O jogo empatou, ambos os jogadores escolheam a mesma opcao.")
elif acao_Humana == "pedra":
    if acao_Bot == "tesoura":
        print("Pedra ganha de tesoura, voce venceu.")
    else:
        print ("Papel ganha de pedra, voce perdeu.")
elif acao_Humana == "papel":
    if acao_Bot == "pedra":
        print("Papel ganha de pedra, voce venceu.")
    else:
        print("Tesoura ganha de papel, voce perdeu.")
elif acao_Humana == "tesoura":
    if acao_Bot == "papel":
        print("Tesoura ganha de papel, voce ganhou.")
    else:
        print("Pedra ganha de tesoura, voce perdeu.")
