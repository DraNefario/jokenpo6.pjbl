import random
print("Escolha jogar com pedra, papel ou tesoura: pedra ganha da tesoura, papel ganha da pedra, tesoura ganha do papel e os iguais empatam")
modoDeJogo = int(input("Digite 1 para jogar humano x máquina, 2 para humano x humano e 3 para máquina x máquina: "))
if modoDeJogo == 1:
    escolhaJogador = input("Digite pedra, papel ou tesoura: ")
    escolhaMaquina = random.choice(["pedra", "papel", "tesoura"])
    print(f"A escolha da máquina foi: {escolhaMaquina}")
    if escolhaJogador == escolhaMaquina:
        print("Empate")
    elif (escolhaJogador == "pedra" and escolhaMaquina == "tesoura") or \
        (escolhaJogador == "papel" and escolhaMaquina == "pedra") or \
        (escolhaJogador == "tesoura" and escolhaMaquina == "papel"):
        print("Você ganhou!")
    else:
        print("Você perdeu :(")