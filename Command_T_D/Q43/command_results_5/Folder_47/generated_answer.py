def find_primes_between_indices(nums):
    return sorted(nums[66:79] for i in range(len(nums)) if all(nums[j] % i != 0 for j in range(i + 1, len(nums) + 1)))
