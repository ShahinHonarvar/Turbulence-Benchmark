def prime_factors(nums):
    primes = set()
    factors = set()
    for i in range(2, int(nums[8]) + 1):
        if all(x % i != 0 for x in nums):
            primes.add(i)
        elif nums[8] % i == 0:
            factors.add(i)
    return factors | primes
