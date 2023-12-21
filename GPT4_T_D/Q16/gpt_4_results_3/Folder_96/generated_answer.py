
def sum_even_ints_inclusive(nums):
    return sum(n for i, n in enumerate(nums[50:201]) if n % 2 == 0)
