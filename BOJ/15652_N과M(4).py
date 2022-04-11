import sys
input = sys.stdin.readline


def perm(depth, N, R):
    if depth == R:
        for i in range(R):
            print(ans[i], end=' ')
        print()
        return

    for i in range(N):
        if depth != 0 and ans[depth-1] > data[i]:
            continue
        ans[depth] = data[i]
        perm(depth+1, N, R)

N, M = map(int, input().split())

data = [i for i in range(1,N+1)]

ans = [0] * M
visit = [0] * N
perm(0,N,M)
