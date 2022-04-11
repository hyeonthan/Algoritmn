import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def findSet(p):
    if p == data[p]:
        return p
    data[p] = findSet(data[p]) # path compression
    return data[p]

def unionSet(a,b):
    ap = findSet(a)
    bp = findSet(b)
    data[bp] = ap

N, M = map(int, input().split())
data = [i for i in range(N+1)]


s = ''
for _ in range(M):
    i,a,b = map(int, input().split())
    if i == 0:
        unionSet(a,b)
    if i == 1:
        if findSet(a) == findSet(b):
            s += 'YES\n'
        else:
            s += 'NO\n'
print(s)

            