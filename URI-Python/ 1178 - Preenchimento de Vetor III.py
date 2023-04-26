entrada = float(input())
lista = []

lista.append(entrada)
aux = entrada

for i in range(0,99):
    aux = aux / 2
    lista.append(aux)
    
cont = 0
for j in lista:
    print(f"N[{cont}] = {j:.4f}")
    cont +=1 