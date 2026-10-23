#TODO Votação de Síndico Um condomínio está elegendo o novo síndico.
#  Existem três candidatos (1 - Ana, 2 - João, 3 - Maria). 
# Crie um programa que receba os votos dos moradores indefinidamente, até que o número 0 seja digitado para encerrar a urna. 
# O programa deve rejeitar votos inválidos (números diferentes de 0, 1, 2 e 3), pedindo que o usuário digite novamente. 
# Ao fim, exiba o total de votos de cada candidato e quem foi o vencedor.


ana = 0
joao = 0
maria = 0

while True:
    voto = int(input("Digite seu voto (1 - Ana, 2 - João, 3 - Maria, 0 - Encerrar): "))

    if voto == 0:
        break
    elif voto == 1:
        ana += 1
    elif voto == 2:
        joao += 1
    elif voto == 3:
        maria += 1
    else:
        print("Voto inválido! Digite 1, 2, 3 ou 0.")

print("\n--- RESULTADO DA VOTAÇÃO ---")
print(f"Votos de Ana: {ana}")
print(f"Votos de João: {joao}")
print(f"Votos de Maria: {maria}")

if ana > joao and ana > maria:
    print("Vencedora: Ana!")
elif joao > ana and joao > maria:
    print("Vencedor: João!")
elif maria > ana and maria > joao:
    print("Vencedora: Maria!")
elif ana == joao == maria:
    print("Houve empate entre os três candidatos!")
else:
    print("Houve empate entre dois candidatos!")


