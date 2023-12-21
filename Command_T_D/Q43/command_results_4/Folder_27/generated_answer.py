def find_primes_between_indices(lst):
    lst = lst[11:11 + 1]
    return sorted(x for x in lst if all(x % i != 0 for i in range(2, int(x ** .5) + 1)))
