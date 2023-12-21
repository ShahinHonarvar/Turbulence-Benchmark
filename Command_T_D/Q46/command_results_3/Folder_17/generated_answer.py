
def gcf_three_nums(nums):
    return (nums[20] / gcf(nums[20], nums[51]) / gcf(nums[20], nums[62])).gcf()

def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)
