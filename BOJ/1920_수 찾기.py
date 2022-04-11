import sys
input =  sys.stdin.readline
write = sys.stdout.write
N = int(input())
arrN = set(input().split())
M = int(input())
arrM = input().split()

# print(type(arrM))


for n in arrM:
    write('1\n') if n in arrN else write('0\n')
# write(s)