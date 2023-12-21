def find_primes_between_indices(list_of_integers):
    list_of_primes = []
    for index in range(19, 91):
        if all(x % y != 0 for x, y in zip(list_of_integers[index:], range(2, int(list_of_integers[index] ** 0.5) + 1))):
            list_of_primes.append(list_of_integers[index])
    return list_of_primes
