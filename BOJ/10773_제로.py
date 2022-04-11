
class Stack:
    def __init__(self):
        self.data = []
    def push(self, v):
        if v == 0:
            self.data.pop()
        else :
            self.data.append(v)
    def sum(self):
        sum = 0
        for i in self.data:
            sum += i
        return sum
s = Stack()
K = int(input())
for i in range(K):
    N = int(input())
    s.push(N)
print(s.sum())