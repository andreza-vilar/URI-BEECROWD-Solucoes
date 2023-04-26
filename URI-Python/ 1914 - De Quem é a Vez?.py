vencedor = []
entrada = int(input())

for i in range(0,entrada):
  dados = input().split()
  jogo = input().split()
  valor = int(jogo[0]) + int(jogo[1])
  if valor % 2 == 0:
    for par in range(len(dados)):
      if dados[par] == "PAR":
        vencedor.append(dados[par -1])
  else:
    for impar in range(len(dados)):
      if dados[impar] == "IMPAR":
        vencedor.append(dados[impar -1])
  valor = 0


for j in vencedor:
  print(j)