def find_primes_between_indices(nums):
    primes = []
    for i in range(1, 6):
        if all(nums[j] % i != 0 for j in range(1, len(nums))):
            primes.append(nums[i])
    return sorted(primes)
