import sys

arr = []

N, M = map(int, input().split())

for i in range(N+M) :
    arr.append(sys.stdin.readline().rstrip())

arr.sort()

result = []
cnt = 0
for i in range(1, N + M) :
    if arr[i] == arr[i-1] :
        cnt += 1
        result.append(arr[i])

print(cnt)
for i in result :
    print(i)