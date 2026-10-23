#TODO Caixa de Supermercado Faça um programa para registrar os itens da compra de um cliente.
#  O programa deve ler o preço e a quantidade de cada item continuamente. 
# Se o preço digitado for negativo, a compra é encerrada. 
# Se o total da compra ultrapassar R$ 200,00, o sistema deve aplicar um desconto de 10% sobre o total.
#  Exiba o valor bruto, o valor do desconto e o valor final a pagar.



total_bruto = 0

while True:
    preco = float(input("Digite o preço do item (negativo para encerrar): R$ "))

    if preco < 0:
        break

    quantidade = int(input("Digite a quantidade: "))

    total_bruto += preco * quantidade


if total_bruto > 200:
    desconto = total_bruto * 0.10
else:
    desconto = 0

total_final = total_bruto - desconto


print("\n--- RESUMO DA COMPRA ---")
print(f"Valor bruto: R$ {total_bruto:.2f}")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor final a pagar: R$ {total_final:.2f}")
