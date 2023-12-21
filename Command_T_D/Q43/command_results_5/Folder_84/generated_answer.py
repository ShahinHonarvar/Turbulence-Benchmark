def find_primes_between_indices(lst):
    lst = lst[830:849+1]
    return sorted(set(lst) - set(lst[1:-1]) - set(lst[2:]))
