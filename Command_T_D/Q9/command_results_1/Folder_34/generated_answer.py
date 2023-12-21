def all_odd_ints_inclusive(nums):
    return [i for i in range(60, 60 + len(nums) // 2, 2) if i in nums]
