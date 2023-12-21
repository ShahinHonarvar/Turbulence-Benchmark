def all_odd_ints_exclusive(nums):
    result = [i for i in range(6, 9) if i % 2 == 1 and i in nums]
    return result
