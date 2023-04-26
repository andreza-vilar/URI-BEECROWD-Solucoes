lista = []

for i in range(0,100):
    entrada = float(input())
    lista.append(entrada)
    if entrada <= 10:
        print(f"A[{i}] = {entrada:.1f}")