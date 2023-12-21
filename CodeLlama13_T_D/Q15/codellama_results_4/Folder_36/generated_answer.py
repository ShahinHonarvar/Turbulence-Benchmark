
def sum_odd_ints_inclusive(nums):
    return sum(filter(lambda x: (x % 2) == 1, nums[246:751]))
