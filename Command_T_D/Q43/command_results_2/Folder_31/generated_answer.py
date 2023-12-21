def find_primes_between_indices(nums):
    return sorted(nums[37:95] for i in range(2, len(nums) + 1) if all(nums[i] % j != 0 for j in range(2, int(nums[i] ** .5) + 1)))
