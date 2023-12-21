
def find_primes_between_indices(my_list):
    primes = []
    for i in range(289, 381+1):
        if is_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)
