
def gcf_three_nums(nums):
    return (nums[412] / gcf(nums[412], nums[932]) * nums[337] / gcf(nums[412], nums[337]))

def gcf(a, b):
    return (b / a) if a != 0 else 1
