def gcf_two_nums(nums):
    return nums[23] // gcf(nums[23], nums[45])
def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)
