def gcf_two_nums(nums):
    return 1 if len(nums) < 2 else nums[47] / gcf(nums[47], nums[10])
def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)
