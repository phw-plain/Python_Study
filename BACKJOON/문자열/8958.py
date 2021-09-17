# OX퀴즈 문제
N = int(input())
answer = []
for i in range(0, N):
    S = list(map(str, input().split()))
    cnt = 0 
    answer.append(0)
    for j in S:
        C = list(map(str, j))
        for k in C:
            if k == 'O':
                cnt+=1
                answer[i]+=cnt
            else :
                cnt = 0
for i in answer:
    print(i)