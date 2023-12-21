def all_odd_ints_inclusive(nums):
    result = [x for x in range(37, 52) if x % 2 == 1]
    return result if result in nums else []
