# 별 찍기-1 문제
N = int(input())
for i in range(0, N):
    str = ""
    for j in range(0, i+1):
        str+="*"
    print(str)  