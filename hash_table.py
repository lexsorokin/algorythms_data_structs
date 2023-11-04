# hash_table (in python dictionary) -> uses hash function to convert a string to an index to see where the element is stored in an array
# works like index but basically allows to use a string representation of an index via unique key 
# look up by key = O(1)
# Insertion and deletion = O(1)

class HashTable: 
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)] # init 100 elems in array

    def get_hash(self, key): 
        h = 0 
        for char in key: 
            h += ord(char) #order of a character
        return h % self.MAX # MOD using size of list 
    
    def __setitem__(self, key, value): # * <- a python operator, that allows to set item like this hd[key] = value 
        h = self.get_hash(key) # get an array index of the key 
        self.arr[h] = value # assign a value to received index of the array

    def __getitem__(self, key): # * <- a python operator, that allows to get item like this hd[key]
        h = self.get_hash(key) # get an array index of the key
        return self.arr[h] # get a value from array by index
    
    def __delitem__(self, key):
        h = self.get_hash(key) 
        self.arr[h] = None 
    
ht = HashTable()
key = "march 6"
hash = ht.get_hash(key)
print(hash)
# ht.add(key=key, value=1234)
ht[key] = 2131521
ht["december 17"] = 25424
ht["march 23"] = 4344
print(ht.arr)
# val = ht.get(key)
print(ht[key])

del ht[key]
print(ht.arr)