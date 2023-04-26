entrada = input().split()
numero = 0

for i in entrada:
  numero = numero + int(i)

numero = numero - len(entrada) + 1

print(numero)