cont = 0
soma = 0

for i in range(0,6):
    entrada = float(input())
    if entrada > 0:
        cont +=1
        soma += entrada

print(f"{cont} valores positivos")
print(f"{soma/cont:.1f}")