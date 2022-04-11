import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
import collections

class Edge:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.cost = c

def findSet(p):
    if p == data[p]:
        return p
    data[p] = findSet(data[p]) # path compression
    return data[p]

def unionSet(a, b):
    ap = findSet(a)
    bp = findSet(b)
    data[ap] = bp

V,E = map(int, input().split())

data = [i for i in range(V+1)]

edgeArr = []
for _ in range(E):
    a,b,c = map(int, input().split())
    edgeArr.append(Edge(a,b,c))

edgeArr = sorted(edgeArr, key = lambda x : x.cost)

value = 0
count = 0
for edge in edgeArr:
    if findSet(edge.a) != findSet(edge.b):
        unionSet(edge.a, edge.b)
        value += edge.cost
        count += 1
        ## 정점의 개수 V보다 작으면 나머지 볼 필요 없음
        if count == V-1:
            break
print(value)