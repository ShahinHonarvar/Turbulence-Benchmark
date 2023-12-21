def prime_factors(nums):
    primes = set()
    for i in range(2, len(nums)):
        if all(nums[i] % j for j in range(3, int(nums[i**0.5]) + 1, 2)):
            primes.add(nums[i])
            for j in range(i**2, len(nums), i):
                primes.update(set(nums[j:]))
    return primes
