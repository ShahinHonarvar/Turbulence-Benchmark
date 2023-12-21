def find_primes_between_indices(nums):
    return sorted(set(range(20, 26)) for i in range(20, 25) if all(nums[j] != i and nums[j] != i**2 for j in range(20, 25)))
