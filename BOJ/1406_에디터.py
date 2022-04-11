import sys

class Stack:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push_s1(self, v):
        self.s1.append(v)

    def push_s2(self, v):
        self.s2.append(v)

    def pop_s1(self):
        return self.s1.pop()
    
    def pop_s2(self):
        return self.s2.pop()

    def isEmpty_s1(self):
        if len(self.s1) == 0:
            return True
        else : return False
    def isEmpty_s2(self):
        if len(self.s2) == 0:
            return True
        else : return False
    
    def print_result(self):
        idx = len(self.s2)
        for i in range(idx):
            self.push_s1(self.pop_s2())
        for i in self.s1 :
            print(i, end="")
s = Stack()

N = input()
for i in str(N):
    s.push_s1(i)
M = int(input())

for i in range(M):
    input_s = sys.stdin.readline().split()
    #input_s = list(map(str, input().split()))
    if input_s[0] == 'P':
        s.push_s1(input_s[1])
    elif input_s[0] == 'L':
        if s.isEmpty_s1() == False :
            s.push_s2(s.pop_s1())
    elif input_s[0] == 'D':
        if s.isEmpty_s2() == False :
            s.push_s1(s.pop_s2())
    elif input_s[0] == 'B':
        if s.isEmpty_s1() == False :
            s.pop_s1()
s.print_result()

