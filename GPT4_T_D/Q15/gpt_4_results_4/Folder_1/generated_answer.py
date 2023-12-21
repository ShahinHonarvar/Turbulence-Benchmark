
def sum_odd_ints_inclusive(nums):
    return sum(num for i, num in enumerate(nums[31:73]) if num % 2 != 0)
