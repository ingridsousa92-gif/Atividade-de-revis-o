#TODO Calculadora de Frete de E-commerce Uma loja virtual precisa de um sistema para calcular o valor do frete.
# crie uma função que receba a distância em quilômetros e o tipo de cliente ("Padrão" ou "VIP")
# Clientes VIP recebem 20% de desconto no valor final do frete.
#  Peça para o usuário inserir os dados e exiba o resultado utilizando a função criada. 


def calcular_frete(distancia, tipo_cliente):
    frete = distancia * 0.50

    if distancia > 100:
        frete += 15.00

    if tipo_cliente.strip().lower() == "vip":
        frete *= 0.80  # Desconto de 20%

    return frete

distancia = float(input("Digite a distância em quilômetros: "))
tipo_cliente = input('Digite o tipo de cliente (Padrão ou VIP): ')

valor_frete = calcular_frete(distancia, tipo_cliente)

print(f"Valor final do frete: R$ {valor_frete:.2f}")
