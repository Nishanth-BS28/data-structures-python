class queue:
    def __init__(self):
        self.st=[]
    def enqueue(self,st):
        self.st.append(st)
    def dequeue(self):
        return self.st.pop(0)
    
#example
q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())