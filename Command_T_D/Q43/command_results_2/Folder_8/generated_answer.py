def find_primes_between_indices(nums):
    return sorted(nums[43:76] for num in nums if all(num % d for d in range(2, int(num ** .5) + 1) if num % d))
