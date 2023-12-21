import functools
@functools.lru_cache(maxsize=2)
def gcf_two_nums(nums):
    x, y = nums[19], nums[94]
    if x == 0:
        return y
    if y == 0:
        return x
    return gcf_two_nums(nums[:19] + nums[20:94] + nums[95:])
