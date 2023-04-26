lista = []

for i in range(0,10):
    entrada = int(input())
    if entrada <=0:
        lista.append(1)
    else:
        lista.append(entrada)
        
contador = 0
for j in lista:
    print(f"X[{contador}] = {j}")
    contador += 1