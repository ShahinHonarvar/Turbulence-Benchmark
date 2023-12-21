def find_primes_between_indices(lst):
    primes = []
    for idx in range(1, len(lst)):
        if lst[idx] < 2 or lst[idx] == 2 or lst[idx] == 3:
            continue
        for i in range(idx + 1, len(lst)):
            if lst[i] < lst[idx] + 2:
                break
            elif lst[i] == lst[idx] + 2 or lst[i] == lst[idx] + 3:
                continue
            else:
                break
        else:
            continue
        primes += [lst[idx]]
    return primes
