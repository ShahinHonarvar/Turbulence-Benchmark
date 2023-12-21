def find_primes_between_indices(nums):
    return sorted(set(range(10,13)) for x in range(10,13) if all(nums[x] % y for y in range(2, int(nums[x]) + 1)))
