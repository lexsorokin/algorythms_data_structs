

def quick_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        base = lst[0]
        less_than = [i for i in lst[1:] if i < base]
        greater_than = [i for i in lst[1:] if i > base]
        return quick_sort(less_than) + [base] + quick_sort(greater_than)
    

lst = [1,6,34,9,25,95,2,67,37]

print(quick_sort(lst))