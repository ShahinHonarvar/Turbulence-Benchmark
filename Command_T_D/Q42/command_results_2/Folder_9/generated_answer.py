def prime_factors(nums):
    primes = set()
    for i in range(2, int(nums[24])+1):
        if all(i not in j for j in nums):
            primes.add(i)
            for j in range(i**2, int(nums[24])+1, i):
                if all(j not in k for k in nums):
                    primes.add(j)
    return primes
