import sys
input = sys.stdin.readline


def perm(depth, N, R):
    if depth == R:
        for i in range(R):
            print(ans[i], end=' ')
        print()
        return

    for i in range(N):
        ## 중복x 순열
        if visit[i] == 0:
            ans[depth] = data[i]
            visit[i] = 1
            perm(depth + 1, N, R)
            visit[i] = 0

N, M = map(int, input().split())

data = [i for i in range(1,N+1)]
print(data)
ans = [0] * M
visit = [0] * N
perm(0,N,M)
