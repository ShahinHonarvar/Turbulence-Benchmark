def find_primes_between_indices(nums):
    return sorted(filter(lambda x: all(x % i for i in range(3, int(x ** .5) + 1, 2)), nums[830:849]))
