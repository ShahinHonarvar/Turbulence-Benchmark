def find_primes_between_indices(lst):
    lst[0] = 2
    for i in range(37, 96):
        if lst[i] == i + 1:
            for j in range(i + 2, 96, i + 1):
                lst[j] = lst[i] + lst[j]
    return sorted(set(lst[37:95]))
