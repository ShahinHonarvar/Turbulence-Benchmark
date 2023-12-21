def find_primes_between_indices(lst):
    primes = []
    for i in range(3, 9):
        if lst[i] == i:
            primes.append(i)
        elif lst[i] == 2:
            primes.append(2)
        elif lst[i] == 1:
            primes.append(1)
    return sorted(primes)
