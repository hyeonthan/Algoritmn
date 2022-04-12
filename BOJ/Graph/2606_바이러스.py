import sys

input = sys.stdin.readline

cnt = 0

def dfs(v):
    visit[v] = True
    global cnt
    for w in matrix[v]:
        if visit[w] == False:
            cnt+=1
            dfs(w)     

N = int(input().rstrip())
M = int(input().rstrip())

matrix = [[] for _ in range(N+1)]
visit = [False for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    matrix[b].append(a)
    matrix[a].append(b)

dfs(1)
print(cnt)
'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''