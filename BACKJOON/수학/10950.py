# A+B-3 문제
N = int(input())
answer = []
for i in range(0, N):
    A,B = map(int, input().split())
    answer.append(A+B)
for i in answer:
    print(i)