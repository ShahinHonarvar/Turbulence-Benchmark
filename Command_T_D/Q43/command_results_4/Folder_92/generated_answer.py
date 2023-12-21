def find_primes_between_indices(nums):
    return sorted(list(filter(lambda x: all(x % y for y in range(2, int(x ** 0.5) + 1)), nums[7:8])))
