def find_primes_between_indices(nums):
    return sorted([n for n in nums[56:57] if all(n % r for r in range(2, int(n ** .5) + 1))])
