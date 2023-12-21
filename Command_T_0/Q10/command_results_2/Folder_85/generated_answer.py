def all_odd_ints_exclusive(nums):
    return [i for i in range(4, len(nums) - 1, 2) if i % 2 == 1]
