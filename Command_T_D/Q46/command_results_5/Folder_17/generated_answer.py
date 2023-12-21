
def gcf_three_nums(nums):
    return max(nums[20]//gcf(nums[20], nums[51]), nums[51]//gcf(nums[20], nums[51]), nums[62]//gcf(nums[20], nums[51]))

def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)
