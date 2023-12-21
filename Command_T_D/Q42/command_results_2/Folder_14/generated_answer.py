def prime_factors(nums):
    primes = set()
    for n in nums:
        if n <= 1:
            continue
        if n <= 3:
            primes.add(n)
            continue
        for i in range(5, int(n ** .5) + 1, 6):
            if n % i == 0:
                primes.add(i)
                break
            if n % (i + 2) == 0:
                primes.add(i)
                break
            if n % (i + 4) == 0:
                primes.add(i)
                break
    return primes
