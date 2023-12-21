def prime_factors(nums):
    primes = set()
    for n in nums:
        if all(n % r != 0 for r in range(2, int(n ** .5) + 1)):
            primes.add(n)
            for i in range(2, int(n ** .5) + 1):
                if n % i == 0:
                    primes.add(i)
                    while n % i == 0:
                        n /= i
    return primes
