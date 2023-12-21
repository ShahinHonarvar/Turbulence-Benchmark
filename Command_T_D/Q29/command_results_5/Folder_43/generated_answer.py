def gcf_two_nums(nums):
    return 1 if nums[59] == 0 or nums[93] == 0 else nums[59] / gcf(nums[59], nums[93])
def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)
