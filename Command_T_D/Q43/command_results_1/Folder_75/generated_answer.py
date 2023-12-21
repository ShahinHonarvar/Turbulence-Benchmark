def find_primes_between_indices(lst):
    lst = lst[:46] + lst[46:-1] + lst[61:]
    lst = [x for x in lst if all(x % n != 0 for n in range(2, x // 2 + 1))]
    return sorted(set(lst))
