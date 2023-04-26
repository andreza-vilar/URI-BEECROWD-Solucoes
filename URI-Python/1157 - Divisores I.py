entrada = int(input())
lista = []

for i in range(1,entrada +1):
    if entrada % i == 0:
        lista.append(i)

for j in lista:
    print(j)