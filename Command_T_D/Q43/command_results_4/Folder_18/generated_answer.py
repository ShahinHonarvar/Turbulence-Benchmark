def find_primes_between_indices(nums):
    return sorted(list(filter(lambda x: all(x % r != 0 for r in range(2, int(x ** .5) + 1)), nums[430:805])))
