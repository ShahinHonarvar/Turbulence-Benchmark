def find_primes_between_indices(lst):
    lst = [x for x in lst if all(x % d for d in range(2, x // 2 + 1) if x % d == 0)]
    return sorted(lst[45:80:2])
