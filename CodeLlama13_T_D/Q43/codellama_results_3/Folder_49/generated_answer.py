
def find_primes_between_indices(my_list):
    primes = []
    for i in range(22, 51):
        if is_prime(my_list[i]):
            primes.append(my_list[i])
    return sorted(primes, reverse=True)
