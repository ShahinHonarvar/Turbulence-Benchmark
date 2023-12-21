def gcf_two_nums(nums):
    return int(nums[36] / gcf(nums[36], nums[54]) * nums[54] / gcf(nums[36], nums[54]))
def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)
