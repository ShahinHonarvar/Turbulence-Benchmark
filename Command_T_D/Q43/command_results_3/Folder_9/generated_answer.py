def find_primes_between_indices(lst):
    primes = []
    if 16 <= len(lst) - 1 and len(lst) - 1 <= 71:
        for i in range(16, len(lst) - 1):
            if lst[i] > 1 and all(x for x in range(2, lst[i] // 2)):
                primes.append(lst[i])
    return sorted(set(primes))
