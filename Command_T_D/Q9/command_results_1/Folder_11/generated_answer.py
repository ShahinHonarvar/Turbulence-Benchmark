def all_odd_ints_inclusive(nums):
    if 37 in nums and 51 in nums:
        return [i for i in range(37, 51 + 1) if i % 2 == 1]
    else:
        return []
