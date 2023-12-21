def prime_factors(nums):
    primes = set()
    for n in nums:
        if all(n % k != 0 for k in range(2, int(n ** .5) + 1)):
            primes.add(n)
    return primes
