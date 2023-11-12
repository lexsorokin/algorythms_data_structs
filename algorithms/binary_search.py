# Time complexity: Log(n)


def binary_search(nums, elem_to_find):
    left_index = 0
    right_index = len(nums) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = nums[mid_index]

        if mid_number == elem_to_find:
            return mid_number

        if mid_number < elem_to_find:
            left_index = mid_index + 1

        else:
            right_index = mid_index - 1

    return -1


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


def recursive_binary_search(lst, find, low = None, high = None):
    low = low
    high = high
    mid = (low + high) // 2
    guess = lst[mid]

    if guess == find:
        return guess, mid
    if guess > find:
        return recursive_binary_search(lst, find, high = mid - 1, low=low)
    else:
        return recursive_binary_search(lst, find, low = mid + 1, high=high)


lst = [i for i in range(1, 100+1)]

print(recursive_binary_search(lst, 67, low=0, high=len(lst)-1))
