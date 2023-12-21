import sys
def gcf_two_nums(nums):
    x = nums[60]
    y = nums[64]
    if x < y:
        return gcf_two_nums(nums[:60] + nums[61:])
    if x == y:
        return x
    return gcf_two_nums(nums[:60] + [x] + nums[61:])
