import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    
    while queue:
        node = queue.popleft()
        if node not in bfs_visit:
            bfs_visit.append(node)
            print(node, end=' ')
            queue.extend(matrix[node])
    #return bfs_visit

def dfs(v):
    dfs_visit[v] = True
    print(v, end=' ')
    for w in matrix[v]:
        if dfs_visit[w] == False:
            dfs(w)
        

N, M, V = map(int, input().split())
matrix = [[] for _ in range(N+1)]
dfs_visit = [False for _ in range(N+1)]
bfs_visit = []


for i in range(M):
    a, b = map(int, input().split())
    matrix[b].append(a)
    matrix[a].append(b)

for i in range(1, N+1):
    matrix[i].sort()

dfs(V)
print()
bfs(V)
# print(bfs(V))


        

    
    