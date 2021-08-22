# 곱셈 문제
A = int(input())
B = int(input())
C = 0
num_arr = [] 
while B != 0: 
    num_arr.append(B%10)
    B=int(B/10)
for i in range(0, len(num_arr)):
    print(A*num_arr[i])
    C+=(A*num_arr[i])*pow(10, i)
print(C)