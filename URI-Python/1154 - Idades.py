soma = 0
cont = 0


while True:
    entrada = int(input())
    if entrada < 0:
        break
    cont += 1
    soma += entrada

media = soma / cont

print(f"{media:.2f}")
    