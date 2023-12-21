
def sum_odd_ints_inclusive(nums):
    return sum(num for i, num in enumerate(nums[310:371]) if num % 2 != 0)
