entrada = int(input())
lista = []

lista.append(entrada)

aux = entrada
for i in range(9):
  aux = aux * 2
  lista.append(aux)
  
cont = 0
for j in lista:
    print(f"N[{cont}] = {j}")
    cont+= 1