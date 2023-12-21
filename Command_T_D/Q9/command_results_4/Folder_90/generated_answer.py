def all_odd_ints_inclusive(nums):
    result = [x for x in range(263, 747, 2) if x in nums]
    return result
