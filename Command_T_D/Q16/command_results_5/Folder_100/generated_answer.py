def sum_even_ints_inclusive(nums):
    sum_even_ints_inclusive = 0
    for i in range(42, 68):
        if nums[i] % 2 == 0:
            sum_even_ints_inclusive += nums[i]
    return sum_even_ints_inclusive
