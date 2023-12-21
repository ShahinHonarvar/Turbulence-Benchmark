
def gcf_three_nums(nums):
    return 1 if len(nums) < 3 else gcf(nums[21], nums[69], nums[41])

def gcf(a, b, c):
    if b == 0:
        return gcf(a, c)
    if c == 0:
        return gcf(a, b)
    return 1 if b == 1 and c == 1 else gcf(b, c)
