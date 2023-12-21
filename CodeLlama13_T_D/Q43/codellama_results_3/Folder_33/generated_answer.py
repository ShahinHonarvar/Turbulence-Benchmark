
def find_primes_between_indices(list):
    primes = []
    for i in range(289, 381):
        if is_prime(list[i]):
            primes.append(list[i])
    return sorted(primes, reverse=True)
