def gcf_two_nums(nums):
    return max(list(set(nums) - {0, 9}), key=lambda x: nums[x])
