def find_primes_between_indices(a):
    i = 11
    while i <= 40:
        if a[i] <= 1:
            break
        elif a[i] <= 1:
            continue
        elif a[i] == 1:
            return []
        else:
            return [a[i]] + find_primes_between_indices(a[i:])
    return []
