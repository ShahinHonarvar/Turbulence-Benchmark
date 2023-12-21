
def sum_odd_ints_inclusive(nums):
    odd_sum = sum(num for i, num in enumerate(nums[533:606]) if num % 2 != 0)
    return odd_sum
