def find_primes_between_indices(lst):
    lst = lst[:]
    primes = []
    for i in range(80, 85):
        for j in range(i + 1, len(lst)):
            if lst[i] % lst[j] == 0:
                break
            else:
                primes.append(lst[i])
    return primes
