class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self._hash_function(key)
        bucket = self.table[hash_key]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))

    def get(self, key):
        hash_key = self._hash_function(key)
        bucket = self.table[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError("key not found")

    def remove(self, key):
        hash_key = self._hash_function(key)
        bucket = self.table[hash_key]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                break
        else:
            raise KeyError("key not found")

    def __str__(self):
        elemets = []
        for bucket in self.table:
            elemets.extend(bucket)

        return '{' + ','.join(f'{k}:{v}' for k, v in elemets) + '}'


# Create a hash table instance
hash_table = HashTable()

# Insert key-value pairs
hash_table.insert('apple', 10)
hash_table.insert('banana', 5)
hash_table.insert('orange', 15)

# Get values using keys
print(hash_table.get('apple'))  # Output: 10
print(hash_table.get('banana'))  # Output: 5
print(hash_table.get('orange'))  # Output: 15

# Remove a key-value pair
hash_table.remove('banana')

# Check the updated hash table
print(hash_table)  # Output: {'apple': 10, 'orange': 15}
