NumeroCorreto = 8
NumeroEscolhido = 75648
while NumeroCorreto != NumeroEscolhido :
    NumeroEscolhido = int(input("Digite um numero de 1 a 10: "))
    if NumeroCorreto > NumeroEscolhido :
        print ("O numero eh maior")
    elif NumeroCorreto == NumeroEscolhido:
        print ("Boa meu")
    else :
        print ("O numero eh menor")

