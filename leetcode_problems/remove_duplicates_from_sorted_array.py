from typing import List

def removeDuplicates(nums: List[int]) -> int:
    n = len(nums)-1    
    insert_index = 1

    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            nums[insert_index] = nums[i]
            insert_index += 1

    return n+1, nums
                


a = [1,1,2]
b = [0,0,1,1,1,2,2,3,3,4]
c = [1,2]

case_one = removeDuplicates(a)
case_two = removeDuplicates(b)
case_three = removeDuplicates(c)

print(case_one)
print(case_two)
print(case_three)