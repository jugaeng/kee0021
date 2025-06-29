list = []

for i in range(7):
    n = int(input())
    if n % 2 == 1:
        list.append(n)
        
if list:
    print(sum(list))
    print(min(list))
else:
    print(-1)