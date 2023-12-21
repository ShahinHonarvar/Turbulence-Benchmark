def sum_even_ints_inclusive(nums):
    return sum(nums[4:4] if even(nums[4:4]) else 0)
def even(nums):
    return nums[::2]
