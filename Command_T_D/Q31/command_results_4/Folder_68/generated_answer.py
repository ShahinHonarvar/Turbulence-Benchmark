def if_perfect_num(nums):
    return nums[3] == 6 and all(nums[0] < nums[i] < nums[i + 1] for i in range(1, len(nums) - 1))
