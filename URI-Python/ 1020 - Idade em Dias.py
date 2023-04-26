entrada = int(input())

ano = entrada // 365
n = entrada - ano*365

m = n // 30
n = n - m*30

d = n

print(f'{ano} ano(s)')
print(f'{m} mes(es)')
print(f'{d} dia(s)')