
def sum_odd_ints_inclusive(nums):
    result = 0
    for i in range(56, 83):
        if nums[i] % 2 != 0:
            result += nums[i]
    return result
