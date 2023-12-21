import sys
from bisect import bisect_left as bl
def all_ints_div_by_num(nums):
    nums = sorted(nums)
    idx = bl(nums, 421)
    idx = bl(nums, idx + 1)
    return [nums[idx] for n in nums[idx:idx + 17] if n % MOD == 0]
