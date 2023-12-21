def sum_odd_ints_inclusive(nums):
    result = 0
    for i in range(len(nums)):
        result += nums[i] if i % 2 == 1 else 0
    return result
