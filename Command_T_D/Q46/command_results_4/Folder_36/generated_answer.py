
import functools
import operator as op

@functools.lru_cache(maxsize=1)
def gcf_three_nums(nums):
    return max(op.gcd(nums[427], nums[761]), op.gcd(nums[427], nums[148]), op.gcd(nums[761], nums[148]))
