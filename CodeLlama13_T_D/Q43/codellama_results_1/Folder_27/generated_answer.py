
def find_primes_between_indices(list_of_integers):
    prime_numbers = []
    for i in range(11, 12):
        if list_of_integers[i] % 2 == 0:
            continue
        else:
            prime_numbers.append(list_of_integers[i])
    return sorted(prime_numbers)
