def gcf_two_nums(nums):
    return 1 if nums[17] == 0 or nums[20] == 0 else gcf(nums[17], nums[20])
def gcf(x, y):
    if y == 0:
        return x
    return gcf(y, x % y)
