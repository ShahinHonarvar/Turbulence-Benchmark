def prime_factors(nums):
    primes = set()
    for i in range(2, int(nums[59]) + 1):
        if all(i % d != 0 for d in range(2, int(i**0.5) + 1)):
            primes.add(i)
            for j in range(i ** 2, int(nums[59]) + 1, i):
                if all(j % d != 0 for d in range(2, int(j**0.5) + 1)):
                    primes.add(j)
    return primes
