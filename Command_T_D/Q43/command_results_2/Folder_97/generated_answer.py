def find_primes_between_indices(nums):
    return sorted(nums[295:455] for i in range(2, len(nums) + 1) if all(nums[j] % i != 0 for j in range(i, len(nums) + 1, i)))
