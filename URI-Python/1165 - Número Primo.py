entrada = int(input())
for j in range(0,entrada):
  n = int(input())
  tot = 0
  for i in range(1,n +1):
    if n % i == 0:
      tot += 1
  if tot == 2:
    print(f"{n} eh primo")
  else:
    print(f"{n} nao eh primo")