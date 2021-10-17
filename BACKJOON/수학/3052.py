# 나머지 문제
N = []
cnt = 0
for i in range(0, 10):
    N.append(int(input())%42)
for i in range(0, 10):
    for j in range(0, 10):
        if N[i] == N[j] and N[i] >= 0 and i != j :
            N[j] = -1
for i in N:
    if i!=-1:
        cnt+=1
print(cnt)