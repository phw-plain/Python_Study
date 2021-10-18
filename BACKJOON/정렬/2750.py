# 수 정렬하기 문제
N = int(input())
num = []
for i in range(0, N):
    num.append(int(input()))
num.sort()
for i in num:
    print(i)