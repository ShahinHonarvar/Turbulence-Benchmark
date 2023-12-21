
def sum_even_ints_inclusive(nums):
    return sum(n for i, n in enumerate(nums) if i <= 1 and n % 2 == 0) or 0
