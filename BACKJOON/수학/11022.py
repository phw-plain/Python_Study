# A+B - 8 문제
T = int(input())
A = []
B = []
for i in range(0, T) : 
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)
for i in range(0, T) :
    print("Case #"+str(i+1)+":",str(A[i]),"+",str(B[i]),"=",str(A[i]+B[i]))