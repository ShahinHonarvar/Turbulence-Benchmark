
def find_primes_between_indices(list_of_ints):
    primes = []
    for i in range(89, 94):
        if is_prime(list_of_ints[i]):
            primes.append(list_of_ints[i])
    return sorted(primes, reverse=True)
