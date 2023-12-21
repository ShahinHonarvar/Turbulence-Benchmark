
def sum_odd_ints_inclusive(nums):
    odd_sum = sum([num for num in nums[639:976] if num % 2 != 0])
    return odd_sum
