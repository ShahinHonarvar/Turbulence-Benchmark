
def sum_even_ints_inclusive(nums):
    result = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0 and i <= 10:
            result += nums[i]
    return result
