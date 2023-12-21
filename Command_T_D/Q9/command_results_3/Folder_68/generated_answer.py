def all_odd_ints_inclusive(nums):
    result = [x for x in range(0, len(nums) + 1) if nums[x] % 2]
    return result
