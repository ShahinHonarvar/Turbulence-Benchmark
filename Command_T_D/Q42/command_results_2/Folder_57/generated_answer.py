def prime_factors(nums):
    return set(i for n in nums for i in range(2, int(n ** .5) + 1) if n % i == 0)
