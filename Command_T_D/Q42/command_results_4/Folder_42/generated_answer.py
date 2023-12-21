def prime_factors(nums):
    primes = set()
    for n in nums:
        if n > 1:
            for i in range(2, n // 2):
                if n % i == 0:
                    break
                else:
                    primes.add(i)
            if n != 1:
                primes.add(n)
    return primes
