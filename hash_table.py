# hash_table (in python dictionary) -> uses hash function to convert a string to an index to see where the element is stored in an array
# works like index but basically allows to use a string representation of an index via unique key 
# look up by key = O(1)
# Insertion and deletion = O(1)

# Collision handling - using linear probing
# Linear probing - basically searching for the next closest slot in the hash table 

class HashTable: 
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for _ in range(self.MAX)] # init 100 elems in array

    def get_hash(self, key): 
        h = 0 
        for char in key: 
            h += ord(char) #order of a character
        return h % self.MAX # MOD using size of list 
    
    def __setitem__(self, key, value): # * <- a python operator, that allows to set item like this hd[key] = value 
        h = self.get_hash(key) # get an array index of the key 
        found = False
        for idx, element in enumerate(self.arr[h]): 
            if len(element) == 2 and element[0] == key: 
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found: 
            self.arr[h].append((key, value))

    def __getitem__(self, key): # * <- a python operator, that allows to get item like this hd[key]
        h = self.get_hash(key) # get an array index of the key
        for element in self.arr[h]: 
            if element[0] == key: 
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key) 
        for index, element in enumerate(self.arr[h]): 
            if element[0] == key: 
                del self.arr[h][index]
    
ht = HashTable()

ht["march 6"]=213
ht["march 5"]=2136
ht["march 17"] = 214
ht["march 6"] = 2145
ht["march 8"] = 123
ht["march 9"] = 1456
 
print(ht["march 17"])
del ht["march 17"]
print(ht.arr)

