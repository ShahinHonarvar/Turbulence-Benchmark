def find_primes_between_indices(list_of_ints):
    primes = []
    for i in range(61, 80):
        if all(x for x in range(2, i // 2) if i % x):
            primes.append(i)
    return sorted(primes)
