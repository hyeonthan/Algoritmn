import sys

read = sys.stdin.readline
write = sys.stdout.write



def merge(s, middle, e):
    ans = []
    i = s
    j = middle + 1
    #k = s
    while i <= middle and j <= e:
        if datas[i] <= datas[j]:
            #ans[k] = datas[i]
            #k += 1
            ans.append(datas[i])
            i += 1
        else :
            # ans[k] = datas[j]
            # k += 1
            ans.append(datas[j])
            j += 1
    
    if i <= middle:
        # for i in range(i, middle+1):
        #     ans[k] = datas[i]
        #     k += 1
        ans += datas[i:middle+1]
    else :
        # for j in range(j, e+1):
        #     ans[k] = datas[j]
        #     k += 1
        ans += datas[j:e+1]
   
    for t in range(len(ans)):
        datas[s] = ans[t]
        s += 1

def merge_sort(s, e):
    if s < e:
        middle = (s+e)//2
        merge_sort(s, middle)
        merge_sort(middle+1, e)
        merge(s,middle, e)


N = int(read().strip())
datas = [int(read().strip()) for _ in range(N)]
#ans = [0] * N

merge_sort(0 , N-1)
for i in range(N):
    write(str(datas[i]) + '\n')