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


def binary_search_recursive(nums, elem_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(nums) or mid_index < 0: 
        return -1
    mid_number = nums[mid_index]

    if mid_number == elem_to_find:
        return f"Elem {mid_number} found at index {mid_index}"

    if mid_number < elem_to_find:
        left_index = mid_index + 1

    else:
        right_index = mid_index - 1

    return binary_search_recursive(nums=nums, elem_to_find=elem_to_find,
                            left_index=left_index, right_index=right_index)


lst = [1, 13, 15, 17, 35, 76, 135, 468]

found = binary_search_recursive(nums=lst, elem_to_find=1, left_index=0, right_index=len(lst))
print(found)