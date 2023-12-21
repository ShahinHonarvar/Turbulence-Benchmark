def find_primes_between_indices(list_of_ints):
    list_of_ints = list(range(6,8))
    list_of_primes = []
    for integer in list_of_ints:
        if all(x % y != 0 for x, y in zip(list_of_ints, range(2, int(integer**(0.5))+1))):
            list_of_primes.append(integer)
    return sorted(list_of_primes)[::-1]
