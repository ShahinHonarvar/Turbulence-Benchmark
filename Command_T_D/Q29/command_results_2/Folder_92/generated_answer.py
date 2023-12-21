def gcf_two_nums(nums):
    return max(list(set(nums[0]) & set(nums[1])), key=lambda x: x)
