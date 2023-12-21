def prime_factors(nums):
    primes = set()
    for i in range(2, int(nums[0] ** 0.5) + 1):
        if all(i not in nums for j in range(len(nums))):
            primes.add(i)
            for j in range(len(nums)):
                if nums[j] % i == 0:
                    primes.update(prime_factors(nums[:j] + nums[j+1:]))
                    break
    return primes
