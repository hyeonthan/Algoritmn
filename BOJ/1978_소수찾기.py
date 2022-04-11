N = int(input())
numbers = list(map(int, input().split()))

cnt = 0
if N == len(numbers):
    for i in numbers:
        if i == 1 : continue
        elif i == 2:
            cnt+=1
        else :
            for n in range(2, i+1):
                if n==i :
                    cnt +=1
                elif i%n == 0:
                    break
print(cnt)


