


def recursive_sum(lst, ind = 0): 

    if ind == len(lst)-1: 
        return lst[ind]
    else: 
        return lst[ind] + recursive_sum(lst, ind=ind+1)



lst = [2,4,6,5,6,8,1,56,8]

print(recursive_sum(lst))