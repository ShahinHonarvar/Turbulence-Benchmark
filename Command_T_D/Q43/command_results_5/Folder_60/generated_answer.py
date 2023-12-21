def find_primes_between_indices(lst):
    lst[0] = lst[1] = 2
    primes = []
    for n in range(46, 85 + 1):
        if all(n % x for x in range(3, int(n ** .5) + 1)):
            primes.append(n)
    return sorted(primes)
