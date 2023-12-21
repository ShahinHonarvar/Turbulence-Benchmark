import math
def prime_factors(nums):
    return set(int(x) for x in range(2, math.ceil(math.sqrt(nums[0]))+1) if all(x % y != 0 for y in range(2, x // 2 + 1)))
