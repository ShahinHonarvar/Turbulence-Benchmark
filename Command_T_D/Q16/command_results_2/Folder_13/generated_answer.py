def sum_even_ints_inclusive(nums):
    result = 0
    for i in range(25, 87, 2):
        if i in nums:
            result += i
    return result
