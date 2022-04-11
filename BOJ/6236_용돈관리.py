import sys
read = sys.stdin.readline
write = sys.stdout.write

def check():
    money = 0
    cnt = 0
    for data in datas:
        if money >= data:
            money -= data
        else:
            money = mid - data
            cnt += 1
    return cnt


N, M = map(int, read().split())
datas = [0] * N
for i in range(N):
    datas[i] = int(read().rstrip())

low = max(datas)
high = 100000000

ans = 0
while low <= high:
    mid = (low + high)//2
    res = check()
    
    if res <= M:
        high = mid - 1
        ans = mid
    else:
        low = mid + 1
print(ans)