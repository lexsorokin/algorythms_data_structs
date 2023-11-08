from typing import List

def rotate(nums: List[int], k: int) -> None:
    # print(f"rotating {nums}...")
    # n = len(nums)
    # if k == 0: 
    #     return
    # for step in range(k): 
    #     current = nums[0]
    #     for i in range(n):
    #         if i == n-1: 
    #             nums[0] = current
    #         else:
    #             save = nums[i+1]
    #             nums[i+1] = current 
    #             current = save

    #     print(f"rotate {step+1} steps to the right: {nums}")
    
    n = len(nums)
    k = k % n  # Ensure k is within the range of the list length

    # Reverse the entire list
    nums[:] = nums[::-1]

    # Reverse the first k elements
    nums[:k] = nums[:k][::-1]

    # Reverse the remaining elements
    nums[k:] = nums[k:][::-1]




nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums, k)

nums =[-1,-100,3,99]
k = 2
rotate(nums, k)