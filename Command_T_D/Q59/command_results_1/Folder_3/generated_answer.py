def all_left_truncatable_prime(nums):
    x = nums[100]
    primes = []
    for num in nums:
        if all(isprime(num - d) for d in range(num, 0, -1)):
            primes.append(num)
    return sorted(primes)
