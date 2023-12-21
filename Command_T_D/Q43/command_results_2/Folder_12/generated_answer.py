def find_primes_between_indices(nums):
    return sorted([i for i in range(16, 25) if all(nums[i] % d != 0 for d in range(3, int(nums[i] ** .5) + 1, 2))])
