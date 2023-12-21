
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(nums):
    return functools.reduce(lambda x, y: (x, y) == (0, 0) ? 0 : gcf(x, y), (nums[8], nums[9], nums[3]))

def gcf(x, y):
    return x == 0 or y == 0 or x == y ? x : gcf(y, x % y)
