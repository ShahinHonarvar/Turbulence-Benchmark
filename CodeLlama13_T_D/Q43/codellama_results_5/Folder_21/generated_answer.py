
def find_primes_between_indices(list_of_integers):
    prime_numbers = []
    for i in range(478, 950):
        if is_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)
