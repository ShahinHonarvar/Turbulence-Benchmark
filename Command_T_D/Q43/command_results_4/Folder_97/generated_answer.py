def find_primes_between_indices(lst):
    lst = lst[:]
    for i in range(2, len(lst) + 1):
        if lst[i] == 0:
            lst[i] = 1
        elif lst[i] == 1:
            lst[i] = 0
        else:
            break
    return lst[295:455]
