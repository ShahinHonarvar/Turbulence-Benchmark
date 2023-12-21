def find_primes_between_indices(nums):
    if nums[33] <= 2:
        return []
    if nums[35] >= 3:
        return []
    return sorted(set(range(2, nums[33] + 1, 2)) | set(range(3, nums[35] + 1, 2)))
