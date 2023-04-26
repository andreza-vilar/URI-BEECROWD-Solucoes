numero = int(input())
dentro = 0
fora = 0

for i in range(0,numero):
    entrada = int(input())
    if entrada >= 10 and entrada <=20 :
        dentro +=1
    else:
        fora +=1

print(f"{dentro} in")
print(f"{fora} out")