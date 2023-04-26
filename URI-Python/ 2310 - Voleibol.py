entrada = int(input())
saques = 0
bloqueios = 0
ataques = 0

saquesFeitos = 0
bloqueiosFeitos = 0
ataquesFeitos = 0

for i in range(0,entrada):
  nome = input()
  tentativas = input().split()
  sucesso = input().split()
  saques += int(tentativas[0])
  bloqueios += int(tentativas[1])
  ataques += int(tentativas[2])
  saquesFeitos += int(sucesso[0])
  bloqueiosFeitos += int(sucesso[1])
  ataquesFeitos += int(sucesso[2])

Sa = saquesFeitos / saques * 100
Bl = bloqueiosFeitos / bloqueios * 100
At = ataquesFeitos / ataques * 100

print(f"Pontos de Saque: {Sa:.2f} %.")
print(f"Pontos de Bloqueio: {Bl:.2f} %.")
print(f"Pontos de Ataque: {At:.2f} %.")