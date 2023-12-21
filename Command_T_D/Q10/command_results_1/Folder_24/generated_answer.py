def all_odd_ints_exclusive(nums):
    if not nums:
        return []
    return [x for x in range(13, 66, 2) if x in nums]
