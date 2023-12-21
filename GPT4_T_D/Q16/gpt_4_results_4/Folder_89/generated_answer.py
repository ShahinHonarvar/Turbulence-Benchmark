
def sum_even_ints_inclusive(nums):
    return sum(num for idx, num in enumerate(nums[56:83]) if num % 2 == 0)
