def prime_factors(nums):
    primes = set()
    for n in nums:
        if n < 2:
            continue
        if all(n % i != 0 for i in range(2, int(n ** .5) + 1)):
            primes.add(n)
            for m in range(2, int(n ** .5) + 1):
                if n % m == 0:
                    primes.add(m)
                    break
        elif n == 2 or n == 3:
            primes.add(n)
    return primes
