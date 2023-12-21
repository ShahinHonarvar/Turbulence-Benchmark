def gcf_two_nums(nums):
    return int(nums[19] / gcf(nums[19], nums[94]) * nums[94] / gcf(nums[19], nums[94]) * gcf(nums[19], nums[94]))
def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)
