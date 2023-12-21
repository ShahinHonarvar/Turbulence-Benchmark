
def sum_even_ints_inclusive(nums):
    even_sum = sum(num for i, num in enumerate(nums[75:89]) if num % 2 == 0)
    return even_sum
