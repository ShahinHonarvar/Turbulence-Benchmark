def find_primes_between_indices(lst):
    return sorted(filter(lambda x: all(x % i for i in range(2, x // 2 + 1)), lst[10:66]))
