# 나는 요리사다 문제
N = M = 0
for i in range(0, 5):
    P = list(map(int, input().split()))
    sum = 0
    for j in P:
        sum += j
    if M < sum:
        M = sum
        N = i+1
print(N, M)