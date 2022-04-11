class Stack:
    def __init__(self):
        self.data = []
        self.size = 10
    
    def push(self, v):
        if len(self.data) == 0 :
            self.data.append(v)
        else :
            if v == self.top():
                self.size += 5
            else :
                self.size += 10
            self.data.append(v)
    def top(self):
        return self.data[-1]

    def sum_size(self) :
        return self.size
s = Stack()
bowl = input()
for i in str(bowl) :
    s.push(i)
print(s.sum_size())