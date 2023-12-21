def gcf_two_nums(nums):
    return 1 if nums[49] == nums[31] else 1 if nums[49] < nums[31] else nums[49] / gcf(nums[49], nums[31])
def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)
