def gcf_two_nums(nums):
    return nums[56] // gcf(nums[56], nums[54])
def gcf(x, y):
    if y == 0:
        return x
    return gcf(y, x % y)
