idade = int(input("Digite sua idade "))
experiencia = input("Digite True se tiver experiencia e False caso contrario ")
AntecedenciasCriminais = input(
    "Digite True se voce tem antecedencias criminais e False se nao ")
EnsinoSuperiorCompleto = input(
    "Digite True se tiver ensino superior completo e False se nao  ")
indicacao = (input("Se tiver incacao digite True caso contrario False "))

if idade >= 18 and AntecedenciasCriminais == "False" and experiencia == "True":
    print("Contratada")
elif experiencia == "False" and (indicacao == "True" or EnsinoSuperiorCompleto == "True") and AntecedenciasCriminais == "False":
    print("Vai pra entrevista")
else:
    print("Aura insuficiente por favor dirija se ate a saida")
