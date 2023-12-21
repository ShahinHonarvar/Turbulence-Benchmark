def find_primes_between_indices(lst):
    lst_idx = [i for i in range(11, 12)]
    primes = []
    for idx in lst_idx:
        lst_idx.append(idx)
        flag = True
        while lst_idx:
            lst_idx.pop()
            if lst[idx] % lst[lst_idx[-1]] == 0:
                flag = False
                break
        if flag:
            primes.append(lst[idx])
    return primes
