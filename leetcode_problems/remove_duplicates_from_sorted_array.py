from typing import List


def removeDuplicates(nums: List[int]) -> int:
    n = len(nums)
    insert_to_index = 1
    has_duplicate = False

    if len(nums) <= 2:
        return len(nums)

    for i in range(1, n):
        if nums[i] != nums[i-1]:
            if has_duplicate:
                nums[insert_to_index] = nums[i]
                insert_to_index += 1
                has_duplicate = False
            else:
                nums[insert_to_index] = nums[i]
                insert_to_index += 1
        elif not has_duplicate:
            has_duplicate = True
            nums[insert_to_index] = nums[i]
            insert_to_index += 1

    return insert_to_index


a = [1, 1, 1, 2, 2, 3]
b = [0, 0, 1, 1, 1, 1, 2, 3, 3]  # -> [0,0,1,1,2,3,3]
c = [1, 2, 2]
d = [1,1,1]

case = removeDuplicates(d)

print(case)
