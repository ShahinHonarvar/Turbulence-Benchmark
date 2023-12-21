def prime_factors(nums):
    primes = set()
    for n in nums:
        if n < 2:
            continue
        if n == 2 or n == 3:
            primes.add(n)
        else:
            for i in range(5, int(n ** .5) + 1, 6):
                if n % i == 0:
                    break
                else:
                    primes.add(i)
            if n > 2 and n % 2 == 0:
                primes.add(2)
            if n > 3 and n % 3 == 0:
                primes.add(3)
    return primes
