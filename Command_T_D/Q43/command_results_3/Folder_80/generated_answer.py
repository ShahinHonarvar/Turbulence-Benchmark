def find_primes_between_indices(lst):
    lst = [x for x in range(13, 30)]
    lst = [x for x in lst if x not in lst[1:]]
    lst = [x for x in lst if all(x % n != 0 for n in range(2, x // 2))]
    return lst
