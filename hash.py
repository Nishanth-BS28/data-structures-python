class hashtable:
    def __init__(self, size=10):
        self.size=size
        self.table=[[] for _ in range(size)]

    def hashf(self, key):
        total=0
        for char in key:
            total += ord(char)
        return total % self.size
    def insert(self, key, value):
        index=self.hashf(key)
        self.table[index].append((key,value))
    def get(self, key):
        index=self.hashf(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
ht = hashtable()
ht.insert("apple", 50)
ht.insert("banana", 30)
ht.insert("cherry", 20)
print(ht.get("apple"))
print(ht.get("banana"))
print(ht.get("grape"))