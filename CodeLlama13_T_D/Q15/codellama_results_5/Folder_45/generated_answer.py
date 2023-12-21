
def sum_odd_ints_inclusive(nums):
    return sum(num for i, num in enumerate(nums) if i >= 30 and i <= 200 and num % 2 == 1) or 0
