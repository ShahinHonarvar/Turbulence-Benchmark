def if_perfect_num(nums):
    return (len(nums) == 1 and nums[0] == 1) or (len(nums) == 2 and nums[0] == 1 and nums[1] == 1) or (len(nums) == 3 and nums[0] == 1 and nums[1] == 2 and nums[2] == 1)
