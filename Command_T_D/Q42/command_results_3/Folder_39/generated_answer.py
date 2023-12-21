import math
def prime_factors(nums):
    if len(nums) == 0:
        return set()
    elif len(nums) == 1:
        return set([nums[0]])
    else:
        return set(prime_factors(nums[:59]) | prime_factors(nums[59:]))
