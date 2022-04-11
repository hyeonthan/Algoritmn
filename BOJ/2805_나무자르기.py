import sys
input = sys.stdin.readline


N, M = map(int, input().split())
datas = list(map(int, input().split()))
# print(datas)
low = 1
high = max(datas)

ans = 0

while low <= high:
    mid = (low + high)//2
    #print("low {} high {} mid {}".format(low, high, mid))
    sum = 0

    for data in datas:
        if data >= mid:
            sum += data - mid
    #print('sum ', sum)
    if sum < M:
        high = mid - 1
      
    elif sum >= M:
        low = mid + 1
        ans = mid
print(ans)
            