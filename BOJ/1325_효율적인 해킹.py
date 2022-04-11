import sys
from collections import deque
input = sys.stdin.readline
write = sys.stdout.write

def bfs(start):
    queue = deque()
    queue.append(start)

    visited = [0] * (N+1)
    visited[start] = 1
    cnt = 0

    while queue:
        v = queue.popleft()
        for w in matrix[v]:
            if visited[w] == 0:
                cnt += 1
                #visited.append(w)
                visited[w] = 1
                queue.append(w)
    return cnt

N, M = map(int, input().split())
matrix = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    matrix[b].append(a)

result = [0] * (N+1)

for i in range(1, N+1):
    result[i] = bfs(i)

s = ''
for i in range(1, N+1):
    if result[i] == max(result):
        s += str(i) + ' '

write(s)