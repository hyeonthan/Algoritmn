# 대장 노드 개수 구하기 for문
import sys
input = sys.stdin.readline

T = int(input())

s = ''
for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        _, _ = map(int, input().split())
    s += str(N-1) + ' '
print(s)

