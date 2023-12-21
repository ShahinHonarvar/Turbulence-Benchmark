def all_odd_ints_inclusive(nums):
    return [i for i in range(len(nums)-1, -1, 2) if i in nums]
