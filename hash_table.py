class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        # hash function from a universal hash function family
        return (hash(key) * 37) % self.size

    def insert(self, key, value):
        hash_key = self._hash_function(key)
        for item in self.table[hash_key]:
            if item[0] == key:
                item[1] = value
                return
        self.table[hash_key].append([key, value])
        print("item inserted", key, value)

    def search(self, key):
        hash_key = self._hash_function(key)
        for item in self.table[hash_key]:
            if item[0] == key:
                return item[1]
        return None

    def delete(self, key):
        hash_key = self._hash_function(key)
        for index, item in self.table[hash_key]:
            if item[0] == key:
                del self.table[hash_key][index]
                return True 
        return False


# Creating a hashtable with size 50
hash_table = HashTable(50)
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
print(hash_table.search("key1"))
print(hash_table.search("key2"))  
hash_table.delete("key1")
print(hash_table.search("key1"))