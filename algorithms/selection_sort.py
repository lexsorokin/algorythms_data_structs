

def find_smallest(lst): 
    smallest = lst[0]
    smallest_index = 0

    for i in range(1, len(lst)):
        if lst[i] < smallest: 
            smallest = lst[i]
            smallest_index = i
    return smallest_index

def sort_array(lst):
    sorted_array = []
    for _ in range(len(lst)):
        smallest = find_smallest(lst)
        sorted_array.append(lst.pop(smallest))
    return sorted_array


lst = [1,6,34,9,25,95,2,67,37]

print(sort_array(lst))