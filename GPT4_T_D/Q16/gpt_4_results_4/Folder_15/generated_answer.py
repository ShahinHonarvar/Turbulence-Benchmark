
def sum_even_ints_inclusive(nums):
    return sum(x for i, x in enumerate(nums[:4]) if x % 2 == 0)
