
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(nums):
    return max(gcf(nums[24], nums[25]), gcf(nums[24], nums[80]), gcf(nums[25], nums[80]))

def gcf(x, y):
    if y == 0:
        return x
    return gcf(y, x % y)
