import sys
input = sys.stdin.readline

N, M = map(int, input().split())

datas = [list(map(int, input().split())) for _ in range(N)]

sum = [[0] * (N+1) for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        sum[j+1][i+1] = sum[j+1][i] + sum[j][i+1] - sum[j][i] + datas[j][i]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = sum[x2][y2] - sum[x2][y1-1] - sum[x1-1][y2] + sum[x1-1][y1-1]
    print(ans)

'''
[1, 3, 6, 10]
[3, 8, 15, 24]
[6, 15, 27, 42]
[10, 24, 42, 64]
'''