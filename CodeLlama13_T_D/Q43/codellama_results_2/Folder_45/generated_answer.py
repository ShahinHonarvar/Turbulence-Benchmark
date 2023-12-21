
def find_primes_between_indices(list_of_ints):
    prime_numbers = []
    for i in range(23, 40):
        if is_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)
