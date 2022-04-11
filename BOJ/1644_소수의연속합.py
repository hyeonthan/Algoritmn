import sys
input = sys.stdin.readline

N = int(input())
arr = [True for _ in range(N+1)]
arr[0], arr[1] = False, False

for i in range(2, N+1):
    if arr[i] == True:
        for j in range(i+i, N+1, i):
            arr[j] = False

datas = [n for n in range(N+1) if arr[n] == True]
datas.append(0)

left = 0
right = 0
sum = 0
ans = 0

while right < len(datas):
    if sum <= N:
        if sum == N:
            ans += 1
        sum += datas[right]
        right += 1
    elif sum > N:
        sum -= datas[left]
        left += 1
print(ans)
