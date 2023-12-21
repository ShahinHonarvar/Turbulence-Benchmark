def find_primes_between_indices(nums):
    return sorted(list(filter(lambda x: all(x % y != 0 for y in range(2, int(x ** .5) + 1)), nums[15:48])))
