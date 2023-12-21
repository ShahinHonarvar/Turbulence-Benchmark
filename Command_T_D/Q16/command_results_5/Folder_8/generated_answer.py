def sum_even_ints_inclusive(nums):
    even_sum = 0
    for i in range(len(nums)-1):
        if i % 2 == 0:
            even_sum += nums[i]
        if i == 23:
            break
    return even_sum
