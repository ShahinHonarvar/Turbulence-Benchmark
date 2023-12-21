def prime_factors(nums):
    primes = set()
    for n in nums:
        if n > 1:
            primes.update(prime_factors(range(2, int(n ** .5) + 1)))
            if n in primes:
                break
    return {n}
