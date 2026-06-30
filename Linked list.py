class node:
    def __init__(self, data):
        self.data=data
        self.next=None
class link:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=new_node

    def display(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next
            
    def prepend(self, data):
        new_node = node(data)
        new_node.next=self.head
        self.head=new_node

    def delete(self, data):
        if self.head.data==data:
            self.head=self.head.next
            return
        current=self.head
        while current.next is not None:
            if current.next.data==data:
                current.next=current.next.next
                return
            current=current.next

#Example
n=link()
n.append(1)
n.append(2)
n.append(3)
n.prepend(0)
n.delete(2)
n.display()