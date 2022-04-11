import sys

input = sys.stdin.readline

K,N = map(int, input().split())

datas = [0] * K
for i in range(K):
    datas[i] = int(input().rstrip())

low = 1
high = max(datas)

ans = 0

while low <= high:
    mid = (low + high) // 2

    cnt = 0

    