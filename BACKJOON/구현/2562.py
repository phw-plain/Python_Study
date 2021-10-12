# 최댓값 문제
N = []
max = 0
cnt = -1
for i in range(1, 10):
    N.append(int(input()))
for i in range(0, 9):
    if max < N[i]:
        max = N[i]
        cnt = i+1
print(max)
print(cnt)