def find_primes_between_indices(lst):
    lst = lst[:38] + lst[38:-2] + lst[54:]
    lst = sorted(set(lst))
    if len(lst) == 0:
        return []
    lst = [x for x in lst if all(x % n != 0 for n in range(2, x // 2 + 1))]
    return lst
