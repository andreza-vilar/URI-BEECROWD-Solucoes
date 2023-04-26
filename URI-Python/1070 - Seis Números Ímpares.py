num = int(input())

if num %2 == 0:
    for i in range(num +1, num + 12,2):
        print(i)
        
else:
    for i in range(num,num + 12,2):
        print(i)