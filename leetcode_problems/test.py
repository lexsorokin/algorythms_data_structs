



def binary_search(lst, find):
    
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]

        if guess == find: 
            return guess
        
        if guess > find: 
            high = mid - 1

        else: 
            low = mid + 1

lst = [i for i in range(1, 100+1)]

print(binary_search(lst, 67))