def all_odd_ints_exclusive(nums):
    result = [i for i in range(51, 76) if i % 2 == 1 and i in nums]
    return result
