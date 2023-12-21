def find_primes_between_indices(lst):
    primes = []
    if lst[6] <= 3:
        primes += [lst[6]]
    elif lst[6] <= 5:
        primes += [lst[6]]
        primes += [lst[7]]
    elif lst[6] <= 7:
        primes += [lst[6]]
        primes += [lst[7]]
        primes += [lst[8]]
    return sorted(set(primes), reverse=True)
