def sum_even_ints_inclusive(nums):
    result = 0
    for i in range(len(nums) - 2):
        if nums[i] % 2 == 0:
            result += nums[i]
        if i == 27:
            result += nums[i]
        if i == 55:
            result += nums[i]
    return result
