
def find_primes_between_indices(my_list):
    primes = []
    for i in range(149, 979+1):
        if my_list[i] not in primes and is_prime(my_list[i]):
            primes.append(my_list[i])
    return sorted(primes)
