def find_primes_between_indices(nums):
    return sorted(filter(lambda x: all(x % y != 0 for y in range(2, x // 2 + 1)), nums[1:5]))
