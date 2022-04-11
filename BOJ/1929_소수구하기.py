# numbers = list(map(int, input().split()))
# resultList = [True for n in range(numbers[1]+1)]
# resultList[0] = False
# resultList[1] = False
# for i in range(2, numbers[1]+1):
#     if resultList[i] == False : continue
#     for j in range(i+i, numbers[1]+1, i):
#         resultList[j] = False;

# for i in range(numbers[0], numbers[1]+1):
#     if resultList[i] == True :
#         print(i)

import sys
input = sys.stdin.readline

M,N = map(int, input().split())

datas = [True for _ in range(N+1)]
datas[0], datas[1] = False, False
for i in range(2, N+1):
    if datas[i] == False: 
        continue
    for j in range(i+i, N+1, i):
        datas[j] = False
print(datas)
for i in range(M, N+1):
    if datas[i] == True:
        print(i)
