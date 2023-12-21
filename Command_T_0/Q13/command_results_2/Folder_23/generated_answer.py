def find_second_largest_num(nums):
    return nums[nums.index(max(nums[:52]) + 1)][nums.index(max(nums[52:71]) + 1)]
