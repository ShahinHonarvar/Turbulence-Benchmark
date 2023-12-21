def find_primes_between_indices(lst):
    primes = []
    for idx in range(24, 32):
        if idx * idx <= lst[idx]:
            continue
        for j in range(idx * 2, lst[idx], idx):
            if lst[j] == j * j:
                continue
            else:
                break
        else:
            primes += [lst[idx]]
    return sorted(primes)
