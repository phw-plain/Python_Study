# 최소, 최대
input()
arr = list(map(int, input().split()))
min = arr[0]
max = arr[0]
for i in arr:
    if min > i:
        min = i
    if max < i:
        max = i
print(min, max)