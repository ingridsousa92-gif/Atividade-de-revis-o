#TODO Avaliação Física de Atletas Um preparador físico precisa avaliar o Índice de Massa Corporal (IMC) de um grupo de atletas.
#  Crie uma função que receba o peso e a altura, calcule o IMC e retorne a classificação (Abaixo do peso, Normal, Sobrepeso, etc.). 
# No programa principal, faça um laço que pergunte os dados de vários atletas. 
# O programa deve parar quando o nome do atleta for "FIM". Ao final, exiba quantos atletas estão na categoria "Normal".


def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    elif imc < 35:
        classificacao = "Obesidade grau I"
    elif imc < 40:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"

    return imc, classificacao


normais = 0

while True:
    nome = input("Digite o nome do atleta (FIM para encerrar): ").strip()

    if nome.upper() == "FIM":
        break

    peso = float(input("Digite o peso em kg: "))
    altura = float(input("Digite a altura em metros: "))

    imc, classificacao = calcular_imc(peso, altura)

    print(f"Atleta: {nome}")
    print(f"IMC: {imc:.2f}")
    print(f"Classificação: {classificacao}")
    print()

    if classificacao == "Normal":
        normais += 1

print(f"Total de atletas na categoria Normal: {normais}")
