def prime_factors(nums):
    primes = set()
    for i in range(2, int(nums[67]) + 1):
        if all(i % j for j in range(2, int(nums[67]) + 1)):
            primes.add(i)
            for j in range(2, i // 2 + 1):
                if i % j == 0:
                    primes.add(j)
                    break
    return primes
