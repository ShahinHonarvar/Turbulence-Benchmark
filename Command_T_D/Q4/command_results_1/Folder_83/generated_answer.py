def all_pos_ints_exclusive(nums):
    if not nums:
        return []
    return [x for x in range(90, 200) if x in nums]
