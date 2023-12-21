def find_primes_between_indices(nums):
    return sorted(set(nums[14:68]) - set(nums[14:-1]) - set(nums[68:]))
