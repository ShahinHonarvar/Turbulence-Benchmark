def find_primes_between_indices(lst):
    return sorted(filter(lambda x: all(x % n != 0 for n in range(2, int(x ** 0.5) + 1)), lst[38:54]), key=lambda x: x)
