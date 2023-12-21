def gcf_two_nums(nums):
    return nums[7] // gcf(nums[7], nums[9])
def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)
