# 곱셈 문제
import math
A, B, C = map(int, input().split())
print(int(math.pow(A, B) % C))