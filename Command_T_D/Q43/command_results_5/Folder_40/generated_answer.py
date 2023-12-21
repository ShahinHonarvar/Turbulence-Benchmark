def find_primes_between_indices(nums):
    primes = []
    for i in range(1, len(nums)):
        if all(nums[i] % j != 0 for j in range(2, int(nums[i] ** 0.5) + 1)):
            primes.append(nums[i])
    return sorted(primes)
