def find_primes_between_indices(lst):
    return sorted(filter(lambda x: x * x <= 459 and all(x % d != 0 for d in range(2, x // 2 + 1)), lst[260:460]))
