def find_primes_between_indices(lst):
    lst = [v for v in lst if v <= 381]
    return sorted([*range(2, len(lst) + 1, 2) if all(v % i for i in range(3, int(v ** .5) + 1, 2))])
