def find_primes_between_indices(nums):
    return sorted(list(filter(lambda x: x > 40 and x <= 68 and all(x % y != 0 for y in range(2, x // 2 + 1))), nums))
