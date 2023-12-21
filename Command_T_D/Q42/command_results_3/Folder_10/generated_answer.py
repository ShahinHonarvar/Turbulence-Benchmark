def prime_factors(nums):
    primes = set()
    for i in range(2, int(nums[54]) + 1):
        if i not in nums:
            primes.add(i)
            for j in range(i**2, int(nums[54]) + 1, i):
                if j not in nums:
                    primes.add(j)
    return primes
