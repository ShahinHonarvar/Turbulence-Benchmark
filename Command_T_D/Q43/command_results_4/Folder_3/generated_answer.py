def find_primes_between_indices(nums):
    return sorted(list(filter(lambda x: all(x % y for y in range(3, int(x ** .5) + 1, 2))), nums[80:84]))
