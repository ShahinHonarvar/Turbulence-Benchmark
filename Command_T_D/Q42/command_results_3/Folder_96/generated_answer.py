def prime_factors(nums):
    primes = set()
    for i in range(2, int(nums[47]) + 1):
        if all(n % i for n in nums):
            primes.add(i)
            for j in range(2, i // 2 + 1):
                if all(n % j for n in nums):
                    primes.add(j)
    return primes
