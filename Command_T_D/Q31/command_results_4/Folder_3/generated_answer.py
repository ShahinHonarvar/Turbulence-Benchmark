def if_perfect_num(nums):
    return all(nums[i] == i + 1 for i in range(len(nums) - 1)) and nums[len(nums) - 1] == 1
