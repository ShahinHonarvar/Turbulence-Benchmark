def find_primes_between_indices(lst):
    idx_primes = []
    for idx in range(15, 48):
        if all(x == 1 or x == lst[idx] for x in range(2, lst[idx] + 1)):
            idx_primes.append(lst[idx])
    return sorted(idx_primes)
