
def find_primes_between_indices(my_list):
    primes = []
    for i in range(13, 29+1):
        if is_prime(i) and i in my_list:
            primes.append(i)
    return sorted(primes, reverse=True)
