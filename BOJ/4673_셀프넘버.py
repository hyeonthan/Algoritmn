list1 = [0 for n in range(10001)]
n = 10;

for i in range(1, 10001):
    tempN = n
    tempV = i
    idx = 0
    idx += tempV
    while(tempN != 1):
        idx += int(tempV/tempN)
        tempV %= tempN
        tempN /= 10
    idx += int(tempV)
    if idx <= 10000:
        list1[idx] = 1
    if i%n == 9:
        n*=10
cnt = 0
for i in range(1, 10001):
    if list1[i]==0:
        print(i)
