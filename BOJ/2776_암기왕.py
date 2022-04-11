import sys
read = sys.stdin.readline



s = ''

T = int(read())

for _ in range(T):
    N = int(read())
    arrN = set(map(int, read().split()))
    M = int(read())
    arrM = list(map(int, read().split()))
    for value in arrM:
        if value in arrN:
            #s += '1\n'
            print(1)
        else:
            # s += '0\n'
            print(0)
#print(s)
