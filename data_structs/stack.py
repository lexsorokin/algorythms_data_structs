from collections import deque

# Stack = Last in First Out (LIFO)
# PUSH/POP element - O(1) 
# Search element by value - O(n)
# Function calling in any programming language is managed using a stack
# In any editor undo (Ctrl+z) functionality in any editor uses stack to track down last set of operations


s = []
s.append("https://www.google.com/")
s.append("https://www.google.com/cats")
s.append("https://www.google.com/dogs")
s.append("https://www.google.com/birds")

# print(s)
# print(s.pop())
# print(s)

# not recommended due to the dynamic nature of the list, which means that
# each time list runs out of the allocated memory slots, it has to copy every thing 
# to a new memory space with an additional len(list) * 2 slots which can be costly depending on the size of the list 

stack = deque() # -> stack using double linked list 

stack.append("https://www.google.com/")
stack.append("https://www.google.com/cats")
stack.append("https://www.google.com/dogs")
stack.append("https://www.google.com/birds")

class Stack: 
    def __init__(self): 
        self.container = deque()

    def push(self, value): 
        self.container.append(value)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    def reverse_string(self, value):        
        return(value[::-1])
    
    def is_balanced(self, value):
        balanced = True
        dct = { 
            "(": 0,
            ")": 0,
            "[": 0,
            "]": 0,
            "{": 0,
            "}": 0,
        }
        for elem in value: 
            if elem in dct:
                dct[elem] += 1
        if dct["("] != dct[")"] or dct["["] != dct["]"] or dct["{"] != dct["}"]:
            balanced = False
        return balanced
            
        
    
stack = Stack()

stack.push("https://www.google.com/")
stack.push("https://www.google.com/cats")
stack.push("https://www.google.com/dogs")
stack.push("https://www.google.com/birds")
# print(stack.size())
# print(stack.peek())
# print(stack.pop())
# print(stack.is_empty())
# print(stack.reverse_string("We will conquere COVID-19"))
print(stack.is_balanced("(()"))