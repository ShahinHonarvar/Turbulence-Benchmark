def find_primes_between_indices(nums):
    return sorted(nums[13:68] for n in range(13, 68) if all(nums[i] != n for i in range(13, n)))
