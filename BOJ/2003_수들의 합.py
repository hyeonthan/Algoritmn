import sys
input = sys.stdin.readline

N,M = map(int, input().split())

arr = list(map(int, input().split()))
arr.append(0)

left = 0
right = 0
sum = 0
ans = 0
while right < N+1:
    if sum <= M:
        if sum == M:
            ans += 1
        sum += arr[right]
        right += 1
    
    if sum > M:
        sum -= arr[left]
        left += 1

print(ans)

# sum = 0
# left = 0
# ans = 0
# for i in range(N):
#     sum += arr[i]

#     while sum >= M:
#         if sum == M:
#             ans += 1
#         sum -= arr[left]
#         left += 1
# print(ans)


        
