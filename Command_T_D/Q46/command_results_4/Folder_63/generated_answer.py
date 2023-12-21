
def gcf_three_nums(nums):
    return max(nums[38] // gcf(nums[38], nums[52]), nums[52] // gcf(nums[38], nums[52]), nums[69] // gcf(nums[38], nums[52]))

def gcf(x, y):
    if x < y:
        return gcf(y, x)
    if x == 1:
        return 1
    return gcf(x // y, y)
