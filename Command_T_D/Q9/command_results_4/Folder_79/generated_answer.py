def all_odd_ints_inclusive(nums):
    result = []
    for i in range(4, len(nums) + 1, 2):
        result += nums[i-4::2]
    return result
