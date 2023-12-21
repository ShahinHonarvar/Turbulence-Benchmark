def find_primes_between_indices(nums):
    return sorted(set(range(10, 13)) for i in range(10, 12) if all(nums[i] % d for d in range(3, int(nums[i]) // 2)))
