import sys
input = sys.stdin.readline

S = input().rstrip()
K = input().rstrip()

newS = ''.join([i for i in S if not i.isdigit()])

HM = [21956]
HK = [17]
HK4 = [1]
ans1 = [0]
ans2 = [0]

n = len(K)
s = '0'
for j in range(1):
    for i in range(n):
        ans1[j] *= HK[j]
        ans2[j] *= HK[j]
        ans1[j] += ord(newS[i])
        ans2[j] += ord(K[i])
        ans1[j] %= HM[j]
        ans2[j] %= HM[j]

        HK4[j] *= HK[j]
        HK4[j] %= HM[j]

    # print(ans1, ans2)
    if ans1 == ans2:
        s = '1'
        break
    for i in range(n, len(newS)):
        ans1[j] *= HK[j]
        ans1[j] -= (ord(newS[i-n])*HK4[j])%HM[j]
        ans1[j] += ord(newS[i])
        ans1[j] += HM[j]
        ans1[j] %= HM[j]
        # print(ans1, ans2)
        if ans1 == ans2:
            s = '1'
            break
print(s)