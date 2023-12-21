def all_pos_ints_exclusive(nums):
    result = list(range(nums.index(36, start=1), nums.index(54, start=1)))
    if not result:
        return []
    return result
