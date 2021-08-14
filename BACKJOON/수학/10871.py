# X보다 작은 수 문제
N, X = map(int, input().split())
num_list = list(map(int, input().split()))
answer = []
for i in num_list:
    if X > i:
        answer.append(i)
for i in answer:
    print(i, end = ' ')