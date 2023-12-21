def all_odd_ints_inclusive(nums):
    result = [i for i in range(0, 5) if i % 2 == 1]
    return result if result in nums else []
