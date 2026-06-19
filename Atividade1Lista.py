Lista = [ "Davi" ,"Gabriel"  ,"John Vector" , "Winderson"]
print(" a lista eh DAVI 0 GABRIEL 1 JOHN VECTOR 2 WINDERSON 3 nessa ordem")
NomeEscolhido = int(input("Digite o numero da lista: "))
if  NomeEscolhido >  3:
    print("O numero eh maior do que a lista")
elif NomeEscolhido < 0:
    print("o numero nn eh negativo")
elif NomeEscolhido == 2:
    print("Boa meu")
    print(Lista[NomeEscolhido])
else:
    print(Lista[NomeEscolhido])
    
