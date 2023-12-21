def find_primes_between_indices(nums):
    return sorted(set(range(37, 96)) for i in range(37, 95) if all(x % y != 0 for x, y in zip(range(i, i + 5), range(2, int(math.ceil(math.sqrt(i)) + 1))))
