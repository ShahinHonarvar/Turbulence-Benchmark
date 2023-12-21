
def gcf_three_nums(nums):
    return 1 if not nums else gcf(nums[20], nums[17], nums[28])

def gcf(x, y, z):
    if x % y == 0:
        return gcf(y, z)
    elif y % z == 0:
        return gcf(x, z)
    elif z % x == 0:
        return gcf(y, x)
    elif z == 0:
        return gcf(x, y)
    else:
        return gcf(y, z)
