def find_primes_between_indices(nums):
    return sorted(list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** .5) + 1)), nums[16:71])))
