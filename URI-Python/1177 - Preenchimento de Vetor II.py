entrada = int(input())
lista = []

for i in range(0,1000):
  aux = 0
  while aux < entrada:
    lista.append(aux)
    aux = aux + 1
  print('N[{0}] = {1}'.format(i,lista[i]))