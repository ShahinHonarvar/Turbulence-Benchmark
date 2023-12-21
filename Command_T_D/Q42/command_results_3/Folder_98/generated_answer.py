def prime_factors(nums):
    return set(int(n) for n in range(2, int(nums[4]) + 1) if all(n % r != 0 for r in range(2, int(n) + 1)))
