def if_perfect_num(nums):
    return all(nums[0] == 1 and nums[1] == 1 and nums[2] == 1 for i in range(len(nums) - 3)) and all(nums[i] == nums[i + 3] for i in range(len(nums) - 6)) and nums[len(nums) - 1] == nums[len(nums) - 2] == nums[len(nums) - 3] == 1
