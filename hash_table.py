#Main Hastable class implementation.
class HashTable:
    # Initialize the hash table with a given size
    def __init__(self, size):
        self.size = size
        # Create a list of empty lists to hold key-value pairs for each hash bucket
        self.table = [[] for _ in range(size)]

    # Hash function to calculate the index for a given key
    def _hash_function(self, key):
        # Hashes the key using a universal hash function and maps it to the table size
        return (hash(key) * 37) % self.size

    # Insert a key-value pair into the hash table
    def insert(self, key, value):
        # Calculate the hash index for the key
        hash_key = self._hash_function(key)
        # Check if the key already exists in the bucket
        for item in self.table[hash_key]:
            if item[0] == key:
                # Update the value if the key exists
                item[1] = value
                return
        # Append the key-value pair to the bucket if key doesn't exist
        self.table[hash_key].append([key, value])
        print("item inserted", key, value)

    # Search for a value associated with a given key
    def search(self, key):
        # Calculate the hash index for the key
        hash_key = self._hash_function(key)
        # Iterate through the bucket to find the key
        for item in self.table[hash_key]:
            if item[0] == key:
                # Return the value if the key is found
                return item[1]
        # Return None if the key is not found
        return None

    # Delete a key-value pair from the hash table
    def delete(self, key):
        # Calculate the hash index for the key
        hash_key = self._hash_function(key)
        # Iterate through the bucket to find the key
        for index, item in enumerate(self.table[hash_key]):
            if item[0] == key:
                # Remove the key-value pair from the bucket if the key is found
                del self.table[hash_key][index]
                return True
        # Return False if the key is not found
        return False


# Creating a hashtable with size 50
hash_table = HashTable(50)
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
print(hash_table.search("key1"))
print(hash_table.search("key2"))  
hash_table.delete("key1")
print(hash_table.search("key1"))