numero = int(input())


anoes = 0
elfos = 0
humanos = 0
magos = 0
hobbits = 0

for i in range(0,numero):
    entrada = input().split()
    if entrada[1] == "A":
        anoes += 1
    elif entrada[1] == "E":
        elfos += 1
    elif entrada[1] == "H":
        humanos += 1
    elif entrada[1] == "M":
        magos += 1
    elif entrada[1] == "X":
        hobbits += 1
        
print(f"{hobbits} Hobbit(s)")
print(f"{humanos} Humano(s)")
print(f"{elfos} Elfo(s)")
print(f"{anoes} Anao(oes)")
print(f"{magos} Mago(s)")