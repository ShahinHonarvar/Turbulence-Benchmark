def find_primes_between_indices(lst):
    lst = lst[:16] + lst[17:71]
    return sorted(set(lst) - set(lst[0] if lst[0] == 2 else lst[:0:-1]) - set(lst[-1] if lst[-1] == 2 else lst[1:]))
