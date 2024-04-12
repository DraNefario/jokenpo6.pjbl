acao_Humana0 = input("Jogador 1, escolha sua jogada (pedra, papel ou tesoura): ")
acao_Humana1 = input("Jogador 2, escolha sua jogada (pedra, papel ou tesoura): ")

print(f"O jogador 1 escolhou {acao_Humana0} e o jogador 2 escolheu {acao_Humana1}.")

if acao_Humana0 == acao_Humana1:
    print(f"O jogo empatou, ambos os jogadores escolheam a mesma opcao.")
elif acao_Humana0 == "pedra":
    if acao_Humana1 == "tesoura":
        print("Pedra ganha de tesoura, o jogador 1 venceu.")
    else:
        print ("Papel ganha de pedra, o jogador 2 venceu.")
elif acao_Humana0 == "papel":
    if acao_Humana1 == "pedra":
        print("Papel ganha de pedra, o jogador 1 venceu.")
    else:
        print("Tesoura ganha de papel, o jogador 2 venceu.")
elif acao_Humana0 == "tesoura":
    if acao_Humana1 == "papel":
        print("Tesoura ganha de papel, o jogador 1 venceu.")
    else:
        print("Pedra ganha de tesoura, o jogador 2 venceu.")