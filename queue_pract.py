from collections import deque

# FIFO = first in first out 

# list representation 

wmt_stock_price_queue = []

wmt_stock_price_queue.insert(0, 131.10)
wmt_stock_price_queue.insert(0, 131.30)
wmt_stock_price_queue.insert(0, 131.50)

# print(wmt_stock_price_queue)

# print(wmt_stock_price_queue.pop()) -> first out
# print(wmt_stock_price_queue.pop()) -> first out
# print(wmt_stock_price_queue.pop())

# Not recommended due to the dynamic nature of list 

# deque representation

q = deque()
q.appendleft(5) # -> appending to the beginning of the list
q.appendleft(7)
q.appendleft(324)

# print(q)

# print(q.pop())
# print(q.pop())
# print(q.pop())

class Queue: 
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val): # place element in the queue
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
q = Queue()


