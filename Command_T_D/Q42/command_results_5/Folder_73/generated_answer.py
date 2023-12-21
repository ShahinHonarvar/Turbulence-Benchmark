def prime_factors(nums):
    primes = set()
    for n in nums:
        if n > 1:
            primes.update(set(range(2, n // 2 + 1)))
            if n % 2 == 0:
                primes.remove(2)
            if n % 3 == 0:
                primes.remove(3)
            for i in range(5, int(n ** .5) + 1, 6):
                if n % i == 0:
                    primes.remove(i)
                    primes.add(n // i)
    return primes
