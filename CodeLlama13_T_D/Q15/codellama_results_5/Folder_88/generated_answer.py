
def sum_odd_ints_inclusive(nums):
    return sum(n for i, n in enumerate(nums) if 4 <= i <= 8 and n % 2 == 1) or 0
