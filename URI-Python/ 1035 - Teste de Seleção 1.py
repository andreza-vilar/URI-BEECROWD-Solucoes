soma = 0
lista = []

entrada = input().split()

for i in entrada:
  lista.append(int(i))

if lista[1] > lista[2]:
    soma += 1
if lista[-1] > lista[0]:
    soma += 1
if lista[2] + lista[-1] > lista[0] + lista[1]:
    soma +=1
if lista[2] > 0 and lista[3] > 0:
    soma += 1
if lista[0] %2 == 0:
    soma += 1

if soma == 5:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")