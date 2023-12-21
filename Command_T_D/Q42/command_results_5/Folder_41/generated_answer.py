def prime_factors(nums):
    primes = set()
    for n in nums:
        if all(n % i != 0 for i in range(2, n // 2)):
            primes.add(n)
    return primes
