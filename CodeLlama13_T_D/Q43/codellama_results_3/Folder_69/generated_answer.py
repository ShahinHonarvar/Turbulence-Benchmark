
def find_primes_between_indices(list_of_integers):
    primes = []
    for i in range(497, 931):
        if is_prime(list_of_integers[i]):
            primes.append(list_of_integers[i])
    return sorted(primes, reverse=True)
