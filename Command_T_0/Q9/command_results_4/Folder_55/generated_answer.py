def all_odd_ints_inclusive(nums):
    return [i for i in range(10, len(nums) + 1, 2) if i in nums]
