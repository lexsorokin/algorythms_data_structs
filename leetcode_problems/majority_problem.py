from typing import List


def majorityElement(nums: List[int]) -> int:  
    st = set(nums)
    majority = nums[0]
    for i in st: 
        if nums.count(i) > nums.count(majority): 
            majority = i
    return majority



a = [3,2,3]
b = [2,2,1,1,1,2,2]
c = [3,3,4]

print(majorityElement(c))