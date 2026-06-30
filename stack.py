class stack:
    def __init__(self):
        self.st=[]
    def push(self,st):
        self.st.append(st)
    def pop(self):
        return self.st.pop()

#Example
s = stack()
s.push("first")
s.push("second")
s.push("third")
print(s.pop())
print(s.pop())