
def sum_odd_ints_inclusive(nums):
    result = 0
    for i in range(246, 751):
        if i < len(nums) and nums[i] % 2 != 0:
            result += nums[i]
    return result
