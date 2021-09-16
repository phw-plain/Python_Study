#  A+B-6 문제
T = int(input())
answer = []
for i in range(0, T) :
    A, B = map(int, input().split(","))
    answer.append(A+B)
for i in answer:
    print(i)