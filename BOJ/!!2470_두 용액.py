import sys
input = sys.stdin.readline

N = int(input())
datas = list(map(int, input().split()))

left = 0
right = 0
sum = 0

while right < N:
