def prime_factors(nums):
    primes = set()
    for n in nums:
        if n == 1:
            continue
        elif n == 2:
            primes.add(2)
            continue
        elif n == 3:
            primes.add(3)
            continue
        for i in range(5, int(n ** .5) + 1, 6):
            if n % i == 0:
                primes.add(i)
                while n % i == 0:
                    n /= i
    return primes
