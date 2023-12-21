def prime_factors(nums):
    primes = set()
    for n in nums:
        if n == 1:
            continue
        elif n == 2 or n == 3:
            primes.add(n)
            continue
        elif n == 4:
            primes.add(2)
            primes.add(3)
            continue
        for i in range(5, int(n ** .5) + 1):
            if n % i == 0:
                primes.add(i)
                break
        else:
            primes.add(n)
    return primes
