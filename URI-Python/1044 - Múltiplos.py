entrada = input().split()
lista = []

for i in entrada:
    lista.append(int(i))
    
if lista[0] % lista[1] == 0 or lista[1] % lista[0] == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")