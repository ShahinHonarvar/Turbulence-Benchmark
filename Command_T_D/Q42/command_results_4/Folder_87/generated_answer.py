def prime_factors(nums):
    primes = set()
    for n in nums:
        if all(n % d == 0 for d in range(3, int(n ** .5) + 1, 2)):
            break
        primes.add(n)
    return primes
