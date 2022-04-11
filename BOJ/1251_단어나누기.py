import sys
input = sys.stdin.readline
write = sys.stdout.write
s = input().rstrip()

idx = 0
start_idx = 0

min = 1000
ans = ''
tmp = s
for i in range(0, len(s)-2):
    if min >= ord(s[i]) and tmp >= s[i::-1]:
        tmp = s[i::-1]
        idx = i
ans += tmp

start_idx = idx+1
min = 1000
tmp = s[start_idx:]
for i in range(start_idx, len(s)-1):
     if min >= ord(s[i]) and tmp >= s[i:start_idx-1:-1]:
        tmp = s[i:start_idx-1:-1]
        idx = i
ans += tmp + s[len(s):idx:-1]

print(ans)
