import functools
@functools.lru_cache(maxsize=10**5)
def gcf_two_nums(nums):
    if len(nums) != 2:
        return None
    a, b = sorted(nums)
    if b == 0:
        return 1
    if a == 0:
        return b
    if a == 1:
        return 1
    if b == 1:
        return a
    if a == b:
        return a
    return 1 if b == 0 else gcf_two_nums([a, b // a])
