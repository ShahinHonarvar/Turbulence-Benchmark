
def sum_even_ints_inclusive(nums):
    sum_even = 0
    for index in range(111, 112):
        if nums[index] % 2 == 0:
            sum_even += nums[index]
    return sum_even
