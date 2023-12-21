def find_primes_between_indices(nums):
    return sorted(set(range(23, 59)) for i in range(23, 59) if all(x % y != 0 for x, y in zip(range(i, 59), nums)))
