def gcf_two_nums(nums):
    nums = sorted(nums)
    return gcf(nums[51], nums[31])
def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)
