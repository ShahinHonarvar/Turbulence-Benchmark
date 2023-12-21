def prime_factors(nums):
    primes = set()
    for n in nums:
        if n > 1:
            for i in range(2, n // 2):
                if n % i == 0:
                    primes.add(i)
                    if i * i != n:
                        primes.add(n // i)
                        break
            else:
                primes.add(n)
    return primes
