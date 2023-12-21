
import functools
import operator
import fractions

@functools.lru_cache(maxsize=1_000_000)
def gcf_three_nums(nums):
    return fractions.gcd(nums[22], nums[97], nums[64])
