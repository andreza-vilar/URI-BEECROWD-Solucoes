entrada = input().split()
maior = 0
lista = []
for c in entrada:
  lista.append(int(c))
  
for i in range(len(lista)):
    if int(lista[i]) > maior:
        maior = lista[i]
    
print(f"{maior} eh o maior")