def gcf_two_nums(nums):
    return max(list(range(min(nums), max(nums) + 1)), key=lambda x: nums[x] // x)
