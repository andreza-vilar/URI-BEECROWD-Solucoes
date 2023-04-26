quantidade = int(input())
resultado = 0
for i in range(0,quantidade):
    entrada = input().split()
    if entrada[1] == "0":
         print("divisao impossivel")
    else:
        resultado = int(entrada[0]) / int(entrada[1])
        print(f"{resultado:.1f}")