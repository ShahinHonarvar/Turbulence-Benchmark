def if_perfect_num(nums):
    return nums[2] == 6 and all(nums[i] == nums[i + 1] for i in range(1, len(nums) - 1))
