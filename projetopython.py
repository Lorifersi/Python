nascimento = 2007
AnoAtual = 2023

def calculoIdade (nascimento, Anoatual):
    idade = AnoAtual - nascimento
    print (idade)
    return idade 

idade = calculoIdade (nascimento, AnoAtual)

print ('idade é ' + str(idade))