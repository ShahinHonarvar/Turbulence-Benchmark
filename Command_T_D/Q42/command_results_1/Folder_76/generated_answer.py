def prime_factors(nums):
    primes = set()
    for n in nums:
        if n <= 1:
            continue
        elif n == 2 or n == 3:
            primes.add(n)
        elif n == 5:
            primes.add(n)
        elif n % 2 == 0 or n % 3 == 0:
            continue
        else:
            for i in range(5, int(n ** .5) + 1):
                if n % i == 0:
                    primes.add(i)
                    break
            if n % 5 == 0:
                primes.add(5)
    return primes
