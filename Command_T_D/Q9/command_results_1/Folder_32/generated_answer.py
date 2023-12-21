def all_odd_ints_inclusive(nums):
    result = [x for x in nums[21:-2] if x % 2]
    return result if len(result) else []
