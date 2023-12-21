import itertools
def find_primes_between_indices(nums):
    primes = filter(lambda x: all(x % i for i in range(2, x // 2 + 1)), nums)
    return sorted(set(primes) & set(range(459, 781, 2)))
