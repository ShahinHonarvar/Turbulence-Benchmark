def prime_factors(nums):
    if len(nums) == 0:
        return set()
    primes = set(range(2, int(nums[0]) + 1))
    for i in range(len(nums)):
        n = int(nums[i])
        for j in range(2, int(n**(0.5)) + 1):
            if n % j == 0:
                primes.add(j)
                for d in range(j + 1, n // j + 1):
                    if n % d == 0:
                        primes.add(d)
                        break
    return primes
