def find_primes_between_indices(nums):
    primes = []
    for i in range(14, 68 + 1):
        if all(nums[i] % k for k in range(3, int(nums[i] ** .5) + 1, 2)):
            primes.append(nums[i])
    return sorted(primes)
