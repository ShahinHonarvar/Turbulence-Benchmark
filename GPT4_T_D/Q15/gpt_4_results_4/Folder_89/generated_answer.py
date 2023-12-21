
def sum_odd_ints_inclusive(nums):
    return sum(num for i, num in enumerate(nums[56:83]) if num % 2 != 0)
