def find_primes_between_indices(nums):
    return sorted([n for n in nums[33:59] if all(n % d for d in range(3, int(n ** .5) + 1, 2))])
