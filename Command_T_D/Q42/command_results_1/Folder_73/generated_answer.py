def prime_factors(nums):
    return set(i for n in nums for i in range(2, n) if n % i == 0)
