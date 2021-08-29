# 팩토리얼 문제
N = int(input())
sum = 1
while N!=0:
    sum*=N
    N-=1
print(sum)