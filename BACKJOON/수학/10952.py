# A+B - 5  문제
answer = []
while True:
    A,B = map(int, input().split())
    if A == 0 and B == 0:
        break
    answer.append(A+B)
for i in answer:
    print(i)