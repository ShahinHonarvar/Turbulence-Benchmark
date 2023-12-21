
def sum_odd_ints_inclusive(nums):
    nums = nums[62:64]
    return sum(num for num in nums if num % 2 != 0)
