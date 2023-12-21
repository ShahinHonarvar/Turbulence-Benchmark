def all_odd_ints_inclusive(nums):
    if not nums:
        return []
    return [x for x in range(len(nums) // 2, -1, 2) if x % 2 == 1]
