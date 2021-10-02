# 별 찍기-2 문제
N = int(input())
for i in range(0, N):
    str = ""
    for j in range(1, N+1):
        if j<(N-i):
            str += " "
        else:
            str+="*"
    print(str)  