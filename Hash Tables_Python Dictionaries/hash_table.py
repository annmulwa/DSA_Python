class HashTable:
    def insert(self, key, value):
        """Insert a new key-value pair"""
        pass

    def find(self, key):
        """Find the value associated with a key"""
        pass

    def update(self, key, value):
        """Change the value associated with a key"""
        pass

    def list_all(self):
        """List all the keys"""
        pass

# create a list size to store key-value pairs
MAX_HASH_TABLE_SIZE = 4096

# set all values to None
data_size = [None] * 4096
print(len(data_size))

# testing
for item in data_size:
    assert item == None

# algorithm for hashing
def get_index(data_list, a_string):
    # result is updated after each iteration
    result = 0

    for a_character in a_string:
       # convert each character in a string to a number
       a_number = ord(a_character)

       # increment the result
       result += a_number

    # return the remainder since the result might be too big than the give size
    list_index = result % len(data_list)

    return list_index

data_list = [None] * 4096

# insert
key, value = 'Mary', '12345'
idx = get_index(data_list, key)
print(ord('M') + ord('a') + ord('r') + ord('y'))
print(idx)
data_list[idx] = (key, value)

data_list[get_index(data_list, 'Paul')] = ('Paul', '23456')

# print(data_list)

# find
idx = get_index(data_list, 'Paul')
print(idx)

key, value = data_list[idx]
print(value)

# list the keys
keys = [kv[0] for kv in data_list if kv is not None]
print(keys)

## creting the hash table
class BasicHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size

    def insert(self, key, value):
        idx = get_index(self.data_list, key)
        data_list[idx] = key, value

    def find(self, key):
        idx = get_index(self.data_list, key)
        kv = data_list[idx]

        if kv is None:
            return None
        else:
            key, value = kv
            return value

    def update(self, key, value):
        idx = get_index(self.data_list, key)
        data_list[idx] = key, value

    def list_all(self):
        # list all the keys
        return [kv[0] for kv in data_list if kv is not None]

basic_table = BasicHashTable(max_size=1024)
print(len(basic_table.data_list) == 1024)

# insert values
basic_table.insert('Ann', '12345')
basic_table.insert('Stacy', '23456')

# find values
print(basic_table.find('Ann'))

# update a value
basic_table.update('Ann', '34567')
print(basic_table.find('Ann'))

# get the list of all keys
keys = basic_table.list_all()
print(keys)

# handling collisions
# e.g "listen" and "silent" have the same characters so they will be at the same index(655)
# we will use a technigue called linear probing to solve this
def get_valid_index(data_list, key):
    idx = get_index(data_list, key)

    while True:
        kv = data_list[idx]

        if kv is None:
            return idx
        k, v = kv
        if k == key:
            return idx

        idx += 1

        if idx == len(data_list):
            idx = 0

data_list1 = [None] * MAX_HASH_TABLE_SIZE
print(get_valid_index(data_list1, 'listen'))
data_list1[get_valid_index(data_list1, 'listen')] = ('listen', 99)
print(get_valid_index(data_list1, 'silent'))

# hash table with linear probing
class ProbingHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size

    def insert(self, key, value):
        idx = get_valid_index(self.data_list, key)
        self.data_list[idx] = key, value

    def find(self, key):
        idx = get_valid_index(self.data_list, key)
        kv = self.data_list[idx]

        if kv is None:
            return None
        else:
            key, value = kv
            return value

    def update(self, key, value):
        idx = get_valid_index(self.data_list, key)
        self.data_list[idx] = key, value

    def list_all(self):
        return[kv[0] for kv in self.data_list if kv is not None]

probing_table = ProbingHashTable(max_size=20)
print(len(probing_table.data_list))
probing_table.insert('pot', 99)

print(probing_table.find('pot') == 99)
probing_table.insert('top', 200)
print(probing_table.find('pot') == 99 and probing_table.find('top') == 200)
print(probing_table.find('pot'))
print(probing_table.find('top'))

probing_table.insert('pot', 101)
print(probing_table.find('pot'))

keys = probing_table.list_all()
print(keys)
