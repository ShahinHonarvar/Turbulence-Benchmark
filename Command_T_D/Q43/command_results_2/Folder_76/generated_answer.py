def find_primes_between_indices(list_of_integers):
    primes = []
    if 149 <= len(list_of_integers) - 1:
        for integer in range(149, len(list_of_integers) - 1):
            if all(integer % n != 0 for n in range(3, int(integer ** .5) + 1)):
                primes.append(integer)
    return sorted(set(primes))
