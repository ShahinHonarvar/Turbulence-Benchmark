
def sum_even_ints_inclusive(nums):
    if len(nums) < 36:
        return 0
    result = 0
    for i in range(33, 37):
        if nums[i] % 2 == 0:
            result += nums[i]
    return result
