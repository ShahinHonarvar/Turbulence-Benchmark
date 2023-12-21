def find_primes_between_indices(nums):
    return sorted([i for i in range(52, 53) if all(nums[i] % d != 0 for d in range(2, int(nums[i**0.5]) + 1))])
