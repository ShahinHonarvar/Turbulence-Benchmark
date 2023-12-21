def gcf_two_nums(nums):
    return 1 if nums[13] == nums[66] else nums[13] / gcf(nums[13], nums[66])
def gcf(a, b):
    return 1 if b == 0 else gcf(b, a % b)
