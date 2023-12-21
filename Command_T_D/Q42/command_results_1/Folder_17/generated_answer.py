import re
def prime_factors(nums):
    factors = set()
    for i in range(0, len(nums)):
        current = nums[i]
        while current != 1:
            factors.add(current)
            current = int(current**0.5)
    return factors
