def prime_factors(nums):
    primes = set()
    for n in nums:
        if n < 2:
            continue
        for i in range(2, int(n ** .5) + 1):
            if n % i == 0:
                break
            elif n == i:
                primes.add(i)
            elif n % i == 1:
                primes.add(i)
                break
    return primes
