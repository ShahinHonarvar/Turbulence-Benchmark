def all_odd_ints_inclusive(nums):
    if 37 <= len(nums) <= 76:
        return [nums[i] for i in range(37, len(nums), 2)]
    else:
        return []
