N = int(input())
N_list = []

for i in range(N):
    N_list.append(int(input()))
    
for i in sorted(N_list):
    print(i)