T = int(input())
contador = 0
lista = []

entrada = input().split()

for i in entrada:
    lista.append(int(i))
    
for j in lista:
    if j == T:
        contador += 1
        

print(contador)