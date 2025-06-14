def find_primes_between_indices(nums):
    primes = []
    for i in range(36, 40):
        if not any(nums[i] % d == 0 for d in range(2, int(nums[i] ** .5) + 1)):
            primes.append(nums[i])
    return sorted(primes, reverse=True)
