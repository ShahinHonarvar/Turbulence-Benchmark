def find_primes_between_indices(lst):
    lst = [x for x in range(19, 86, 2) if x * x <= 85]
    return sorted(x for x in lst if all(x % d == 0 for d in range(2, x // 2 + 1)))
