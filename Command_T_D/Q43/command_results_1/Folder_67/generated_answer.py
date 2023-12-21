def find_primes_between_indices(lst):
    lst = list(range(17, 80))
    if not lst:
        return []
    lst = [v for v in lst if all(v % i for i in range(3, int(v ** .5) + 1, 2)) and v not in lst[1:]]
    return sorted(set(lst))
