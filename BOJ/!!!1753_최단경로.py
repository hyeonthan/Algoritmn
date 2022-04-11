import heapq

V,E = map(int, input().split())
start = int(input())
INF = 0x7fffffff

arr = [[] for i in range(V+1)]

for i in range(E):
    u,v,w = map(int, input().split())
    arr[u].append((v, w))

ans = [INF for i in range(V+1)]

def dijkstra():
    qData = []
    ans[start] = 0 # 시작점 갱신

    heapq.heappush(qData,(0,start)) # 시작점 큐에 넣기

    while qData:
        cost, pos = heapq.heappop(qData) # 큐에 노드 정보 꺼내기

        if ans[pos] < cost:        # 과거에 교체된 노드라면 버리자
            continue

        for c in arr[pos]:          # 이 노드의 인접리스트 정보 
            w = c[0]                # nextPos
            wCost = c[1]            # nextPos 가는 비용
            if ans[w] > ans[pos] + wCost:   # 주변 갱신
                ans[w] = ans[pos] + wCost   # 업데이트 성공이면
                heapq.heappush(qData, (ans[w], w))  # 큐에 삽입
dijkstra()
for i in range(1, V+1):
    if ans[i] == INF:
        print("INF")
        continue
    print(ans[i])