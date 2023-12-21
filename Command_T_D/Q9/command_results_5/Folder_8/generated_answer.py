def all_odd_ints_inclusive(nums):
    result = [x for x in nums[23:]]
    result += [x for x in nums[0:23] if x % 2 == 1]
    return result
