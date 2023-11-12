# Time complexity: Log(n)


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


def recursive_binary_search(lst, find, low=None, high=None):
    low = low
    high = high
    mid = (low + high) // 2
    guess = lst[mid]

    if guess == find:
        return guess, mid
    if guess > find:
        return recursive_binary_search(lst, find, high=mid - 1, low=low)
    else:
        return recursive_binary_search(lst, find, low=mid + 1, high=high)


lst = [i for i in range(1, 100+1)]

print(recursive_binary_search(lst, 67, low=0, high=len(lst)-1))
