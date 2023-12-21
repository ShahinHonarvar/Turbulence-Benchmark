def find_primes_between_indices(nums):
    return sorted(nums[11:11+5] for i in range(11, 11+5) if all(nums[i] % j != 0 for j in range(3, int(nums[i] ** 0.5) + 1, 2)))
