def find_primes_between_indices(nums):
    return sorted(nums[55:87] for i in range(55, 87) if all(nums[i] % r != 0 for r in range(2, int(nums[i**0.5]) + 1)))
