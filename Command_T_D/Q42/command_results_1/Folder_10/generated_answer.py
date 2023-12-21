def prime_factors(nums):
    primes = set()
    for n in nums:
        if n < 2:
            continue
        elif n == 2 or n == 3:
            primes.add(n)
            continue
        for i in range(2, int(n**(0.5)) + 1):
            if n % i == 0:
                primes.add(i)
                if n != i**2:
                    primes.add(n // i)
                break
    return primes
