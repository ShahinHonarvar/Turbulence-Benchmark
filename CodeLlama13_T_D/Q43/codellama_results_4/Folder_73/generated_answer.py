
def find_primes_between_indices(list_of_integers):
    prime_numbers = []
    for i in range(19, 91):
        if list_of_integers[i] == 0:
            break
        elif is_prime(list_of_integers[i]):
            prime_numbers.append(list_of_integers[i])
    return sorted(prime_numbers, reverse=True)
