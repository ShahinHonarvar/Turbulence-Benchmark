
def sum_even_ints_inclusive(nums):
    return sum(num for i, num in enumerate(nums) if 25 <= i <= 59 and num % 2 == 0)
