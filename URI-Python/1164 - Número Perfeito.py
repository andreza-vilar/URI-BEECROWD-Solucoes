entrada = int(input())
soma = 0
for i in range(0,entrada):
    soma = 0
    numero = int(input())
    for j in range(1,numero):
        if numero % j == 0:
            soma += j
    if soma == numero:
        print(f"{numero} eh perfeito")
    else:
        print(f"{numero} nao eh perfeito")