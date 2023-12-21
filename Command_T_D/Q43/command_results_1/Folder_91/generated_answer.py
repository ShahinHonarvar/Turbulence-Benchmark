def find_primes_between_indices(nums):
    return sorted(nums[0] if nums[0] % 2 == 0 and nums[1] == 2 or nums[0] == 3 else nums[0])
