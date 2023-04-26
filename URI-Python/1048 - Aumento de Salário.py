entrada = float(input())

porc = 0
novo = 0
reajuste = 0

if entrada > 0 and entrada <= 400.00:
    porc = 15
    novo = entrada * 1.15
    reajuste = novo - entrada
    print(f"Novo salario: {novo:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {porc} %")
    
elif entrada > 400.00 and entrada <= 800.00:
    porc = 12
    novo = entrada * 1.12
    reajuste = novo - entrada
    print(f"Novo salario: {novo:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {porc} %")

elif entrada > 800.00 and entrada <= 1200.00:
    porc = 10
    novo = entrada * 1.10
    reajuste = novo - entrada
    print(f"Novo salario: {novo:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {porc} %")

elif entrada > 1200.00 and entrada <= 2000.00:
    porc = 7
    novo = entrada * 1.07
    reajuste = novo - entrada
    print(f"Novo salario: {novo:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {porc} %")

elif entrada > 2000.00:
    porc = 4
    novo = entrada * 1.04
    reajuste = novo - entrada
    print(f"Novo salario: {novo:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {porc} %")