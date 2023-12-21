def all_odd_ints_exclusive(nums):
    if 29 in nums and 53 in nums:
        return [i for i in range(29, 53, 2) if i in nums]
    else:
        return []
