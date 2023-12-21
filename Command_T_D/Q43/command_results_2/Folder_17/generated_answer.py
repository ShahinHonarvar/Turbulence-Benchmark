def find_primes_between_indices(lst):
    start, stop = 15, 48
    primes = []
    for num in range(start, stop + 1):
        if all(num % d == 0 for d in range(2, int(num ** .5) + 1)):
            break
        primes.append(num)
    return sorted(set(primes))
