
def sum_odd_ints_inclusive(nums):
    return sum(x for i, x in enumerate(nums[14:65]) if x % 2 != 0)
