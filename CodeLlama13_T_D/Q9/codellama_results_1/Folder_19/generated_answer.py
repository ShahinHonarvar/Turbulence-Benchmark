
def all_odd_ints_inclusive(nums):
    return [n for i, n in enumerate(nums) if 3 <= i <= 5 and n % 2 == 1]
