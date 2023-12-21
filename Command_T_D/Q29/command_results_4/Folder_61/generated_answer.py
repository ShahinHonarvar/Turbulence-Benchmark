def gcf_two_nums(nums):
    return max(list(set(nums[8:].union(nums[:3]))))
