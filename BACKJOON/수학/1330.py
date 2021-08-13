# 두 수 비교하기 문제
A, B = input().split()
A = int(A)
B = int(B)
if A > B :
    print('>')
else :
    if A < B :
        print('<')
    else :
        print('==')