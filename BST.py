class node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
class bst:
    def __init__(self):
        self.root=None
    def insert(self, data):
        new_data=node(data)
        if self.root is None:
            self.root=new_data
            return
        current=self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left=new_data
                    return
                current=current.left
            else:
                if current.right is None:
                    current.right=new_data
                    return
                current=current.right
    def search(self, data):
        current=self.root
        while current is not None:
            if current.data==data:
                return True
            elif data < current.data:
                    current=current.left 
            else:
                current=current.right
        return False
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)
#Example
b=bst()
b.insert(1)
b.insert(5)
b.insert(8)
b.insert(45)
b.insert(23)
b.insert(6)
b.inorder(b.root)
print(b.search(5))
print(b.search(8))

