
def find_primes_between_indices(list_of_integers):
    prime_numbers = []
    for i in range(27, 86+1):
        if is_prime(list_of_integers[i]):
            prime_numbers.append(list_of_integers[i])
    return sorted(prime_numbers, reverse=True)
