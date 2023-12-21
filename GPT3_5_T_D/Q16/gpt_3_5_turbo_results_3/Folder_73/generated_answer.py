
def sum_even_ints_inclusive(nums):
    even_sum = 0
    for num in nums[19:93]:
        if num % 2 == 0:
            even_sum += num
    return even_sum
