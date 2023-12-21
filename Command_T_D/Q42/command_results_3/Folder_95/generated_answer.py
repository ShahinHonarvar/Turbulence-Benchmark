def prime_factors(nums):
    primes = set()
    for n in nums:
        if n == 1:
            continue
        if n == 2 or n == 3:
            primes.add(n)
        for i in range(2, int(n ** .5) + 1):
            if n % i == 0:
                primes.add(i)
                break
    return primes
