
def find_primes_between_indices(lst):
    prime_numbers = []
    for i in range(23, 49):
        if is_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)
