def sum_even_ints_inclusive(nums):
    even_sum = 0
    for i in range(21, 97, 2):
        if i in nums:
            even_sum += i
    return even_sum
