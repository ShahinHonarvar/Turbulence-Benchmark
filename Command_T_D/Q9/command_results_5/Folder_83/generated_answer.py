def all_odd_ints_inclusive(nums):
    result = [y for x in range(90, 200, 2) for y in nums[x::2]]
    return result
