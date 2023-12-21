
def find_primes_between_indices(my_list):
    prime_numbers = []
    for i in range(41, 86):
        if is_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)
