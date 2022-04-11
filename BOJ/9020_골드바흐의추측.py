import sys
input = sys.stdin.readline
write = sys.stdout.write
T = int(input())

datas = [int(input().rstrip()) for _ in range(T)]

idx = max(datas) + 1
arr = [True for _ in range(idx)]
arr[0], arr[1] = False, False

for i in range(2, idx):
    if arr[i] == False:
        continue
    for j in range(i+i, idx, i):
        arr[j] = False

s= ''
for data in datas:
    idxA = data//2
    idxB = data//2
    while idxA >=0 and idxB < data:
        if arr[idxA] and arr[idxB]:
            write(str(idxA) + ' ' + str(idxB) + '\n')
            break
        idxA -= 1
        idxB += 1