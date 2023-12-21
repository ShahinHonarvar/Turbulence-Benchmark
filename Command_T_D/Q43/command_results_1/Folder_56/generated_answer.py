def find_primes_between_indices(nums):
    return sorted(nums[40:68]) if nums[40] <= nums[68] and all(nums[40:68]) else []
