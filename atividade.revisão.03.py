#TODO Controle de Qualidade na Fábrica Em uma linha de produção, as peças passam por uma balança.
# O operador informará o peso de  peças (pergunte ao usuário quantas peças serão pesadas antes de iniciar).
# Sem utilizar listas, crie um programa que determine e exiba no final 
# qual foi o peso da peça mais pesada e  qual foi o peso da peça mais leve que passou pela esteira naquele lote. 


quantidade = int(input("Quantas peças serão pesadas? "))

for i in range(1, quantidade + 1):
    peso = float(input(f"Digite o peso da peça {i} (kg): "))

    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso

        if peso < menor_peso:
            menor_peso = peso

if quantidade > 0:
    print(f"\nPeso da peça mais pesada: {maior_peso:.2f} kg")
    print(f"Peso da peça mais leve: {menor_peso:.2f} kg")
else:
    print("Nenhuma peça foi pesada.")
