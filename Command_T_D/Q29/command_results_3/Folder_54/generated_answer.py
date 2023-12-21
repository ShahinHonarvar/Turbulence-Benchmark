def gcf_two_nums(nums):
    return (nums[56] / gcf(nums[56], nums[92]) + nums[92] / gcf(nums[56], nums[92]) - 1) / 2
def gcf(x, y):
    while y:
        x, y = y, x % y
    return x
