import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

cnt = 0  
def subSet(depth, N, S):
    global cnt
    if depth == N:
        sum = 0
        for i in range(N):
            if visit[i] == 1:
                sum += visit[i]
                print(data[i], end=' ')
        if sum == S:
            cnt += 1
        print()
        return
    visit[depth] = 0
    subSet(depth + 1, N, S)
    visit[depth] = 1
    subSet(depth +1, N, S)

N, S = map(int, input().split())

data = list(map(int, input().split()))

visit = [0] * N
subSet(0, N, S)
print(cnt)

