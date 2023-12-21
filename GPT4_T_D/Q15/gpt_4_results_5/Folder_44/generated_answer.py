
def sum_odd_ints_inclusive(nums):
    return sum(num for index, num in enumerate(nums[13:69]) if num % 2 != 0)
