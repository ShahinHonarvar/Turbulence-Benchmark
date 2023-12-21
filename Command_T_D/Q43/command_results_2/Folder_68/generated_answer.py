def find_primes_between_indices(nums):
    return sorted([x for x in nums if all(x % i for i in range(2, int(x ** .5) + 1))])
