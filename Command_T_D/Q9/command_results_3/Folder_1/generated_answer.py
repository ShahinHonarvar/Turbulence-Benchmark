def all_odd_ints_inclusive(nums):
    return [i for i in range(31, 73) if i % 2 == 1 and i in nums]
