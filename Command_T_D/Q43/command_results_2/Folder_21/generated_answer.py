def find_primes_between_indices(nums):
    primes = []
    for n in nums[478:949]:
        if all(n % d != 0 for d in range(2, n // 2)):
            primes.append(n)
    return sorted(primes)
