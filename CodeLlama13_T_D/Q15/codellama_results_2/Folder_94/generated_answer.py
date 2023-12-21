
def sum_odd_ints_inclusive(nums):
    return sum(x for i, x in enumerate(nums) if i >= 28 and i <= 40 and x % 2 == 1) or 0
