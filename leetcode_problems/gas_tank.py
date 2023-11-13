def canJump(nums: list[int]) -> bool:

    n = len(nums) - 1
    jump_from = 0
    
    for i in range(jump_from, n):
        if nums[i] == 0: 
            return False
        for j in range(nums[i]): 
            if j + nums[j] >= n: 
                return True
            jump_from = max(nums[i:i*2])
            

        


nums = [2,3,1,1,4]

print(canJump(nums))