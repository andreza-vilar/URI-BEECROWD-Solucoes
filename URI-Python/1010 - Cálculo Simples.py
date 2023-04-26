linha1 = input().split()
cod1 = int(linha1[0])
numero1 = int(linha1[1])
valor1 = float(linha1[2])

linha2 = input().split()
cod2 = int(linha2[0])
numero2 = int(linha2[1])
valor2 = float(linha2[2])

total = (numero1 * valor1) + (numero2 * valor2)

print(f"VALOR A PAGAR: R$ {total:.2f}")