import sys
input = sys.stdin.readline

N, M= map(int, input().split())
datas = list(map(int, input().split()))
sum = [0] * N

for i in range(0, N):
    if i == 0:
        sum[i] = datas[i]
    else:
        sum[i] += sum[i-1] + datas[i]
for _ in range(M):
    s, e = map(int, input().split())
    if s-2 < 0:
        print(sum[e-1])
    else:
        print(sum[e-1] - sum[s-2])