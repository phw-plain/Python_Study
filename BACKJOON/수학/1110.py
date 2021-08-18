# 더하기 사이클 문제
N = int(input())
A = int(N/10)
B = N%10 
temp = -1
cnt = 0
while temp != N:
    temp = B * 10 + int((A+B)%10)
    A = int(temp/10)
    B = temp%10
    cnt += 1
print(cnt)