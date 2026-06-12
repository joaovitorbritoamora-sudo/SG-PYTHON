import random
NumeroLimite = int(input("Vamos fazer um jogo de 1 ate o numero: "))
NumeroChances = int(input("Escolha um numero de chances: "))
NumeroCorreto = random.randint(1, NumeroLimite)
NumeroEscolhido = 75648
while NumeroCorreto != NumeroEscolhido and NumeroChances >= 1:
    NumeroEscolhido = int(input("Digite um numero: "))
    if NumeroCorreto > NumeroEscolhido:
        print("O numero eh maior")
    elif NumeroCorreto == NumeroEscolhido:
        print("Boa meu")
    else:
        print("O numero eh menor")
    NumeroChances -= 1
    if NumeroChances == 0:
        print("as suas chances acabaram. o numero certo era", NumeroCorreto)
