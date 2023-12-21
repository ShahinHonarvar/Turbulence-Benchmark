def find_primes_between_indices(nums):
    primes = [x for x in range(23, 60) if all(x % y for y in range(2, x // 2)) and x not in nums]
    return sorted(primes) if primes else []
