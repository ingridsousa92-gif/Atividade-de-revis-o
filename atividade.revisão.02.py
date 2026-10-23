#TODO Monitoramento de Temperatura em Estufa Um agricultor possui uma estufa e um sensor de temperatura que faz leituras constantes.
#  Escreva um programa que leia continuamente a emperatura registrada (em graus Celsius) 
# até que o usuário digite um valor de parada (por exemplo, -99).
#  Ao final, o programa deve exibir:A temperatura média do período. 
# Quantas vezes a temperatura ultrapassou a marca de perigo (acima de 35°C).


soma_temperaturas = 0
quantidade = 0
temperaturas_perigo = 0

while True:
    temperatura = float(input("Digite a temperatura em °C (-99 para parar): "))

    if temperatura == -99:
        break

    soma_temperaturas += temperatura
    quantidade += 1

    if temperatura > 35:
        temperaturas_perigo += 1

if quantidade > 0:
    media = soma_temperaturas / quantidade

    print(f"\nTemperatura média: {media:.2f} °C")
    print(f"Temperaturas acima de 35 °C: {temperaturas_perigo}")
else:
    print("Nenhuma temperatura foi registrada.")
