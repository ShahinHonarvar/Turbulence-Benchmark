def all_odd_ints_exclusive(nums):
    if 11 <= len(nums) <= 76:
        return [x for x in nums[11:-1]]
    else:
        return []
