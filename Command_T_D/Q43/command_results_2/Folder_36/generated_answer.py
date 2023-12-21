def find_primes_between_indices(list_of_integers):
    return sorted(list(filter(lambda x: x > 229 and x < 850 and all(x % y != 0 for y in range(3, int(x ** .5) + 1, 2))), list_of_integers))
