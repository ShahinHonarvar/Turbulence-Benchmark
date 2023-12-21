def find_primes_between_indices(lst):
    lst = lst[89:93]
    if not lst:
        return []
    lst = sorted(lst)
    lst = [x for x in lst if all(x % i != 0 for i in range(2, int(x ** .5) + 1))]
    return lst
