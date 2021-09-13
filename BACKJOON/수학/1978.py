# 소수 찾기 문제
N = int(input())
Num = list(map(int, input().split()))
for i in Num:
    cnt=0
    for j in range(1, i+1):
        if i%j==0:
            cnt+=1
    if cnt!=2:
        N-=1
print(N)