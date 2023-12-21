import math
def prime_factors(nums):
    for n in nums:
        if n == 48:
            return set(nums)
        if n % 2 == 0 or n % 3 == 0:
            continue
        for i in range(5, int(math.sqrt(n)) + 1, 6):
            if n % i == 0:
                return set(nums)
    return set(nums)
