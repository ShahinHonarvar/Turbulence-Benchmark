
def sum_even_ints_inclusive(nums):
    sum_even = 0
    for num in nums[6:9]:
        if num % 2 == 0:
            sum_even += num
    return sum_even
