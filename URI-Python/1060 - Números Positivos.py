positivo = 0

for i in range(0,6):
    ent = float(input())
    if ent > 0:
        positivo += 1
        
print(f"{positivo} valores positivos")