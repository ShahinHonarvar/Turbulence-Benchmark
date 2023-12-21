def if_perfect_num(nums):
    return all(nums[i] < nums[i + 1] for i in range(len(nums) - 1)) and nums[80] == sum(nums)
