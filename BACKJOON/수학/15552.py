# 빠른 A+B 문제
import sys
N = int(input())
answer = []
for i in range(0, N):
    A, B = map(int, sys.stdin.readline().split())
    answer.append(A+B)
for i in answer:
    print(i)